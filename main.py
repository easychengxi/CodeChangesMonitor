#Import modules
from emailing import SendEmail
from monitoring import monitor
from webscreen import screenshot

#Monitor webs
webs = ['https://www.cms.gov/Medicare/Coding/HCPCSReleaseCodeSets/HCPCS-Quarterly-Update',
        'https://www.cms.gov/Medicare/Coding/ICD10',
        'https://www.cms.gov/medicare/icd-10/2022-icd-10-cm',
        'https://www.cms.gov/medicare/icd-10/2022-icd-10-pcs',
        'https://www.ama-assn.org/practice-management/cpt',
        'https://www.ama-assn.org/practice-management/cpt/category-i-vaccine-codes',
        'https://www.ama-assn.org/practice-management/cpt/category-iii-codes',
        'https://www.ama-assn.org/practice-management/cpt/cpt-pla-codes'
        ]

def main(webs):
    monitor(webs)

if __name__ == '__main__':
    main(webs)

