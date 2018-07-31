from connection import DBConnection
import feedparser
import json
import xlrd


data_source_xl = ("data_source.xlsx")
 
wb = xlrd.open_workbook(data_source_xl)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
data_source_list =	{}
for i in range(sheet.nrows):
	if (i > 0 and sheet.cell_value(i, 6) == "ACT"):
		data_source_rows =	{
		"ds_id": int(sheet.cell_value(i, 0)),
		"ds_template": sheet.cell_value(i, 1),
		"ds_group": sheet.cell_value(i, 2),
		"ds_sub_group": sheet.cell_value(i, 3),
		"ds_category": sheet.cell_value(i, 4),
		"ds_url": sheet.cell_value(i, 5),
		}
		data_source_list[int(sheet.cell_value(i, 0))] = data_source_rows
		
with open('data_source.json', 'w') as f:
	json.dump(data_source_list, f, ensure_ascii=False)
	

for i in range(sheet.nrows):
	if (i > 0 and sheet.cell_value(i, 6) == "ACT"):
		feed_item_by_ds_id = []	
		feed_data = feedparser.parse(sheet.cell_value(i, 5))
		if(sheet.cell_value(i, 2) == 'digit'):
			for each in feed_data['entries']:
				feed_item =	{
				"ds_id": int(sheet.cell_value(i, 0)),
				"title": each['title'],
				"link": each['link'],
				"summary": each['summary'],
				"media": each['media_thumbnail'][0]['url'],
				"author": each['author_detail'],
				"published": each['published_parsed'],
				}
				feed_item_by_ds_id.append(feed_item);
				#with open('feed_item.json', 'w') as f:
					#json.dump(feed_item, f, ensure_ascii=False)
				#break
		#print(feed_item_by_ds_id)		
		with open(str(int(sheet.cell_value(i, 0)))+".json", 'w') as f:	
			json.dump(feed_item_by_ds_id, f, ensure_ascii=False)
	
#
#with open('data.json', 'w') as f:
	#json.dump(d['entries'][0], f, ensure_ascii=False)
  
#print (d['entries'][0])
#for each in d['entries']:
#	print (each['title'])
#with open('feed_item.json', 'w') as f:
#			json.dump(each, f, ensure_ascii=False)