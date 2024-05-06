from soar.clientmanager.client_data_manager import ClientDataManager

client_data = {
    "Brand_Information": [
        {
            "Name": "Brand A",
            "Country": "Brazil",
            "Language": "Portuguese",
            "Web_Domain": "www.branda.com",
            "Legal_Entity": "Legal Entity A",
            "Tax_ID": "123456789",
            "Logo": "logo1.png",
            "Google_Play_ID": "id_google_play_a",
        },
        {
            "Name": "Brand B",
            "Country": "United States",
            "Language": "English",
            "Web_Domain": "www.brandb.com",
            "Legal_Entity": "Legal Entity B",
            "Tax_ID": "987654321",
            "Logo": "logo3.png",
            "Google_Play_ID": "id_google_play_b",
        },
    ],
    "Security_Information": [
        {
            "Name": "exit",
            "Login_Pages": [
                "login.branda.com",
                "logindsadsa.branda.com",
                "login.branda.com",
                "login.brandb.com",
            ],
            "dsa": [
                "login.branda.com",
                "logindsadsa.branda.com",
                "login.branda.com",
                "login.brandb.com",
            ],
            "keywords": ["caju", "wpds"],
            "Third_Party_Login_Pages": ["thirdpartylogin.com", "anotherlogin.com"],
            "Safelist": {
                "Allowed_Domains": ["branda.com", "brandb.com", "thirdpartylogin.com"],
                "Allowed_IP_Addresses": ["192.168.1.1", "192.168.1.2", "10.0.0.1"],
                "Allowed_Email_Domains": ["example.com"],
            },
            "APIs": [
                {"Name": "thehive_internal_mods_api", "api_key": "192.168.1.1"},
                {"Name": "caju", "api_key": "192.168.1.2"},
            ],
        }
    ],
    "Executive_Information": [
        {
            "Name": "Executive Name 2",
            "Variations": ["Abbreviated Name 2", "Full Name with Second Surname 1"],
            "Emails": ["email1@example.com", "email2@example.com"],
            "Identification": {
                "ID_Card": "XX.XXX.XXX-X",
                "SSN": "XXX.XXX.XXX-XX",
                "Driver_License": "XXXXXXX",
                "Passport": "XX1234567",
            },
            "Phones": ["(11) 99999-9999", "(11) 88888-8888"],
            "Cards": {
                "Credit": ["1234 5678 9123 4567", "2345 6789 1234 5678"],
                "Debit": ["3456 7891 2345 6789"],
            },
            "Social_Media": {
                "Facebook": "facebook.com/executiveName1",
                "Instagram": "@executiveName1",
                "outros": "@executiveName1",
                "LinkedIn": "linkedin.com/in/executiveName1",
            },
        },
        {
            "Name": "Executive Name3",
            "Variations": ["Abbreviated Name 2", "Full Name with Second Surname 1"],
            "Emails": ["email1@example.com", "email2@example.com"],
            "Identification": {
                "ID_Card": "XX.XXX.XXX-X",
                "SSN": "XXX.XXX.XXX-XX",
                "Driver_License": "XXXXXXX",
                "Passport": "XX1234567",
            },
            "Phones": ["(11) 99999-9999", "(11) 88888-8888"],
            "Cards": {
                "Credit": ["1234 5678 9123 4567", "2345 6789 1234 5678"],
                "Debit": ["3456 7891 2345 6789"],
            },
            "Social_Media": {
                "Facebook": "facebook.com/executiveName1",
                "Instagram": "@executiveName1",
                "outros": "@executiveName1",
                "LinkedIn": "linkedin.com/in/executiveName1",
            },
        },
    ],
}

if __name__ == "__main__":
    from connect_modules.mongoconnect import MongoDBClientManager

    # Instanciando o gerenciador do MongoDB
    client_manager = MongoDBClientManager("mongodb://localhost:27017/")
    client_data_manager = ClientDataManager(client_manager, "cawwwwju")
    client_data_manager.create_and_populate_collections(client_data)
    client_manager.close()
