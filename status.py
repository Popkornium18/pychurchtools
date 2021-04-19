"""
Status
======

CRUD methods for status field

These are the statuses that a person can have.
(e.g. "Visitor", "Friend", "Member", etc.)

"""

from ct_types import CTStatus
from typing import Any, List, Optional


class Status:

    def __init__(self, ct: Any) -> None:
        """Initialize a Status object.
        """

        self.__ct = ct

    def get_all(self) -> List[CTStatus]:
        """Get all statuses from the API.

        :returns: A list of all status
        :rtype: List[CTStatus]
        """

        res = self.__ct.make_request('statuses')

        statuses = []
        if res and 'data' in res:
            for item in res['data']:
                statuses.append(CTStatus(**item))

        return statuses

    def get(self, status_id: int) -> Optional[CTStatus]:
        """Get a status by ID.

        :param status_id: The ID of the status
        :type status_id: int
        :returns: The status
        :rtype: CTStatus
        """

        route = f'statuses/{status_id}'
        res = self.__ct.make_request(route)

        if res and 'data' in res:
            return CTStatus(**res['data'])

        return None
