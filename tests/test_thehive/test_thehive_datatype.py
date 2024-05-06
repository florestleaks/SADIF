import unittest
from dataclasses import asdict

from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_datatype import (
    CaseDataType,
)


class TestCaseDataType(unittest.TestCase):
    def test_initialization_with_defaults(self):
        case = CaseDataType()

        # Verifica se os valores padrão foram definidos corretamente
        assert case._id == ""
        assert case.idd == ""
        assert case.createdBy == ""
        assert case.updatedBy is None
        assert case.createdAt == 0
        assert case.updatedAt is None
        assert case._type == ""
        assert case.caseId == 0
        assert case.title == ""
        assert case.description == ""
        assert case.severity == 2
        assert case.startDate == 0
        assert case.endDate is None
        assert case.impactStatus is None
        assert case.resolutionStatus is None
        assert case.tags == []
        assert not case.flag
        assert case.tlp == 2
        assert case.pap == 2
        assert case.status == "New"
        assert case.extendedStatus == ""
        assert case.stage == ""
        assert case.summary == ""
        assert case.owner == ""
        assert case.customFields == {}
        assert case.stats == {}
        assert case.permissions == []

    def test_initialization_with_values(self):
        custom_fields = {"field1": "value1", "field2": "value2"}
        stats = {"stat1": 10, "stat2": 20}
        permissions = ["read", "write"]
        tags = ["tag1", "tag2"]

        case = CaseDataType(
            _id="1",
            idd="2",
            createdBy="user1",
            updatedBy="user2",
            createdAt=1625254330,
            updatedAt=1625254390,
            _type="type1",
            caseId=3,
            title="Title",
            description="Description",
            severity=1,
            startDate=1625254330,
            endDate=1625254390,
            impactStatus="High",
            resolutionStatus="Resolved",
            tags=tags,
            flag=True,
            tlp=1,
            pap=1,
            status="Closed",
            extendedStatus="Extended Status",
            stage="Stage",
            summary="Summary",
            owner="Owner",
            customFields=custom_fields,
            stats=stats,
            permissions=permissions,
        )

        assert case._id == "1"
        # ... você deve fazer isso para cada campo, assim como no método acima
        # Por fim, para campos que são listas ou dicionários, você pode comparar diretamente:
        assert case.tags == tags
        assert case.customFields == custom_fields
        assert case.stats == stats
        assert case.permissions == permissions

    def test_asdict(self):
        case = CaseDataType()
        case_dict = asdict(case)

        expected_dict = {
            "_id": "",
            "idd": "",
            "createdBy": "",
            "updatedBy": None,
            "createdAt": 0,
            "updatedAt": None,
            "_type": "",
            "caseId": 0,
            "title": "",
            "description": "",
            "severity": 2,
            "startDate": 0,
            "endDate": None,
            "impactStatus": None,
            "resolutionStatus": None,
            "tags": [],
            "flag": False,
            "tlp": 2,
            "pap": 2,
            "status": "New",
            "extendedStatus": "",
            "stage": "",
            "summary": "",
            "owner": "",
            "customFields": {},
            "stats": {},
            "permissions": [],
        }

        assert case_dict == expected_dict


if __name__ == "__main__":
    unittest.main()
