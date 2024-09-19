import json
import re

def convert_to_numeric(value):
    if isinstance(value, str):
        # Remove "억원" and any spaces, then convert to float
        numeric_value = re.sub(r'[^\d.]', '', value.replace('억원', ''))
        return float(numeric_value) if numeric_value else None
    return value

# Read the JSON data from the file
with open('innoforest_data.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Define the fields we want to include and their readable names
fields = {
    'corpId': 'Company ID',
    'corpNameKr': 'Company Name (Korean)',
    'corpNameEn': 'Company Name (English)',
    'corpIntroKr': '기업설명',
    'finacRevenueVal': '매출',
    'invstSumValText': '누적투자금액 (억원)',
    'empWholeVal': '직원수',
    'bizNamesKr': '카테고리',
    'tagNamesKr': '키워드'
}

# Open a file for writing
with open('output.tsv', 'w', encoding='utf-8') as outfile:
    # Write the header
    outfile.write('\t'.join(fields.values()) + '\n')

    # Write the data
    for item in json_data:
        row = []
        for field in fields.keys():
            value = item.get(field, '')
            if field == 'invstSumValText':
                value = convert_to_numeric(value)
            row.append(str(value))
        outfile.write('\t'.join(row) + '\n')

print("Data conversion complete. Results saved in 'output.tsv'. Open this file and copy its contents to paste into Google Sheets.")
