import unittest

from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_case_comment_template import (
    CaseCommentTemplate,
)


class TestCaseCommentTemplate(unittest.TestCase):
    def test_malicious_dns_alert_template(self):
        expected_template = [
            {"type": "header", "value": {"level": 1, "text": "Alerta de DNS Malicioso"}},
            {
                "type": "header",
                "value": {"level": 2, "text": "Domínio Suspeito: {dominio_suspeito}"},
            },
            {
                "type": "unordered_list",
                "value": [
                    "IP associado: {ip_associado}",
                    "Registrado em: {data_registro}",
                    "Atualizado em: {data_atualizacao}",
                ],
            },
        ]

        assert expected_template == CaseCommentTemplate.MALICIOUS_DNS_ALERT


if __name__ == "__main__":
    unittest.main()
