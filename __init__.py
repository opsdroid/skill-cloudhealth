import logging
import asyncio
import aiohttp
from datetime import datetime

from opsdroid.matchers import match_apiai_action, match_crontab, match_regex
from opsdroid.message import Message

_LOGGER = logging.getLogger(__name__)
CHAPI_ENDPOINT = "https://chapi.cloudhealthtech.com/olap_reports"


################################################################################
# Helper functions                                                             #
################################################################################


async def get_aws_cost_for_period(api_key, period):
    """Returns the amount spent in the previous period."""
    url = "{}/cost/history?api_key={}&interval={}".format(CHAPI_ENDPOINT, api_key, period)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                response = await resp.json()
                return round(response['data'][-1][0][0], 2)


################################################################################
# Skills                                                                       #
################################################################################


@match_crontab("00 09 * * *")
@match_regex("AWS bill yesterday")
async def aws_billing_daily(opsdroid, config, message):
    """Skill to announce yesterday's total billing from CloudHealth."""
    if message is None:
        if not config.get("monthly-billing-alerts", True):
            return
        connector = opsdroid.default_connector
        room = config.get("room", connector.default_room)
        message = Message("", None, room, connector)
    api_key = config.get("chapi-key", None)
    if api_key is not None:
        cost = await get_aws_cost_for_period(api_key, "daily")
        await message.respond("Yesterday we spent £{:,} on AWS.".format(cost))
    else:
        await message.respond("I can't check the billing API without a key.")


@match_crontab("00 09 01 * *")
@match_regex("AWS bill last month")
async def aws_billing_daily(opsdroid, config, message):
    """Skill to announce last month's total billing from CloudHealth."""
    if message is None:
        if not config.get("monthly-billing-alerts", True):
            return
        connector = opsdroid.default_connector
        room = config.get("room", connector.default_room)
        message = Message("", None, room, connector)
    api_key = config.get("chapi-key", None)
    if api_key is not None:
        cost = await get_aws_cost_for_period(api_key, "monthly")
        await message.respond("Last month we spent £{:,} on AWS.".format(cost))
    else:
        await message.respond("I can't check the billing API without a key.")