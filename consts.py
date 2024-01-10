NONE = 'O'
PAD = "[PAD]"

train_data = "data/train.json"
dev_data = "data/dev.json"
test_data = "data/test.json"
wordemb_file = 'data/100.utf8'

batch_size = 8
lr = 1e-3
n_epochs = 30

MAXLEN = 50
WORD_DIM = 100
ENTITY_DIM = 50
POSTAG_DIM = 50
POSITION_DIM = 50


# # 34 event triggers
# TRIGGERS = ['Business:Merge-Org',
#             'Business:Start-Org',
#             'Business:Declare-Bankruptcy',
#             'Business:End-Org',
#             'Justice:Pardon',
#             'Justice:Extradite',
#             'Justice:Execute',
#             'Justice:Fine',
#             'Justice:Trial-Hearing',
#             'Justice:Sentence',
#             'Justice:Appeal',
#             'Justice:Convict',
#             'Justice:Sue',
#             'Justice:Release-Parole',
#             'Justice:Arrest-Jail',
#             'Justice:Charge-Indict',
#             'Justice:Acquit',
#             'Conflict:Demonstrate',
#             'Conflict:Attack',
#             'Contact:Phone-Write',
#             'Contact:Meet',
#             'Personnel:Start-Position',
#             'Personnel:Elect',
#             'Personnel:End-Position',
#             'Personnel:Nominate',
#             'Transaction:Transfer-Ownership',
#             'Transaction:Transfer-Money',
#             'Life:Marry',
#             'Life:Divorce',
#             'Life:Be-Born',
#             'Life:Die',
#             'Life:Injure',
#             'Movement:Transport']

# 30 event triggers
TRIGGERS = ['ATTACK.Arbitrary_Code_Execution', 
            'ATTACK.DoS', 
            'ATTACK.Root_Compromise', 
            'ATTACK.Spyware', 
            'ATTACK.Trojan', 
            'ATTACK.User_Compromise', 
            'ATTACK.Viruss', 
            'ATTACK.Web_Compromise', 
            'ATTACK.Worms', 
            'DISCOVER.Back_door', 
            'DISCOVER.Buffer_Overflow', 
            'DISCOVER.Incorrect_Permission', 
            'DISCOVER.Insufficient_Authentication_Validation', 
            'DISCOVER.Kernel_Flaws', 
            'DISCOVER.Misconfiguration', 
            'DISCOVER.SQLI', 
            'DISCOVER.Social_Engineering', 
            'DISCOVER.XSS', 
            'IMPACT.Breach', 
            'IMPACT.Destruct', 
            'IMPACT.Disrupt', 
            'IMPACT.Distort', 
            'PATCH.Back_door', 
            'PATCH.Buffer_Overflow', 
            'PATCH.Incorrect_Permission', 
            'PATCH.Insufficient_Authentication_Validation', 
            'PATCH.Kernel_Flaws', 
            'PATCH.Misconfiguration', 
            'PATCH.SQLI', 
            'PATCH.XSS']

# # 5 event triggers
# TRIGGERS = ["Databreach", 
#             "Phishing", 
#             "Ransom", 
#             "PatchVulnerability",
#             "DiscoverVulnerability"]

# # 54 entities
# ENTITIES = ['VEH:Water',
#             'GPE:Nation',
#             'ORG:Commercial',
#             'GPE:State-or-Province',
#             'Contact-Info:E-Mail',
#             'Crime',
#             'ORG:Non-Governmental',
#             'Contact-Info:URL',
#             'Sentence',
#             'ORG:Religious',
#             'VEH:Underspecified',
#             'WEA:Projectile',
#             'FAC:Building-Grounds',
#             'PER:Group',
#             'WEA:Exploding',
#             'WEA:Biological',
#             'Contact-Info:Phone-Number',
#             'WEA:Chemical',
#             'LOC:Land-Region-Natural',
#             'WEA:Nuclear',
#             'LOC:Region-General',
#             'PER:Individual',
#             'WEA:Sharp',
#             'ORG:Sports',
#             'ORG:Government',
#             'ORG:Media',
#             'LOC:Address',
#             'WEA:Shooting',
#             'LOC:Water-Body',
#             'LOC:Boundary',
#             'GPE:Population-Center',
#             'GPE:Special',
#             'LOC:Celestial',
#             'FAC:Subarea-Facility',
#             'PER:Indeterminate',
#             'VEH:Subarea-Vehicle',
#             'WEA:Blunt',
#             'VEH:Land',
#             'TIM:time',
#             'Numeric:Money',
#             'FAC:Airport',
#             'GPE:GPE-Cluster',
#             'ORG:Educational',
#             'Job-Title',
#             'GPE:County-or-District',
#             'ORG:Entertainment',
#             'Numeric:Percent',
#             'LOC:Region-International',
#             'WEA:Underspecified',
#             'VEH:Air',
#             'FAC:Path',
#             'ORG:Medical-Science',
#             'FAC:Plant',
#             'GPE:Continent']

# 24 entities
ENTITIES = ['ORGANIZATION', 
            'CAUSE_OF_DEATH', 
            'DATE', 
            'NATIONALITY', 
            'DURATION', 
            'NUMBER', 
            'CITY', 
            'LOCATION', 
            'PERSON', 
            'MISC', 
            'MONEY', 
            'COUNTRY', 
            'TITLE', 
            'TIME', 
            'CRIMINAL_CHARGE', 
            'ORDINAL', 
            'URL', 
            'STATE_OR_PROVINCE', 
            'PERCENT', 
            'SET', 
            'IDEOLOGY', 
            'RELIGION', 
            'EMAIL', 
            'HANDLE']

# 45 pos tags
# POSTAGS = ['JJ', 'NNS', 'IN', 'VBG', 'NNP', ':', 'VBZ', '.', 'UH', ',', 'PRP', 'MD', 'VB', 'RB', 'DT', 'NN', 'VBP', 'RP', 'PRP$', 'VBD', 'CD', 'HYPH', 'WRB', 'WP', 'VBN', 'CC', 'EX', 'TO', 'NNPS', '-LRB-', '-RRB-', 'PDT', 'WDT', 'JJS', 'RBR', 'POS', '$', '``', "''", 'JJR', 'RBS', 'WP$', 'NFP', 'AFX', 'ADD', 'SYM', 'FW', 'GW', 'LS']

# 49 pos tags
POSTAGS = ['PRP', 'VBP', 'IN', 'NNS', 'VBD', 
           'VBN', 'VBG', 'DT', ',', 'CC', 
           'RB', 'NN', 'JJ', '.', 'NNP', 
           'JJS', 'RP', 'POS', 'CD', 'VBZ', 
           'HYPH', 'WDT', '-LRB-', '-RRB-', 'TO', 
           'VB', 'PRP$', ':', '``', 'MD', 
           'RBR', 'NNPS', 'WP', '$', 'JJR', 
           "''", 'WRB', 'SYM', 'ADD', 'EX', 
           'RBS', 'NFP', 'UH', 'PDT', 'LS', 
           'FW', 'AFX', 'GW', 'WP$']