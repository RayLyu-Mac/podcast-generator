import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml','r') as f:
  yamlDt=yaml.safe_load(f)

  rsse=xml_tree.Element('rss',{
    'version':'2.0',
   'xmlns:itunes':'http://www/itunes.com/dtds/podcast-1.0.dtd',
   'xmlns:content':'http://purl.org/rss/1.0/modules/content/'
  })

channelE=xml_tree.SubElement(rsse,'channel')

link_prefix=yamlDt['link']
xml_tree.SubElement(channelE,'title').text=yamlDt['title']
xml_tree.SubElement(channelE,'format').text=yamlDt['format']
xml_tree.SubElement(channelE,'subtitle').text=yamlDt['title']
xml_tree.SubElement(channelE,'itunes:author').text=yamlDt['author']
xml_tree.SubElement(channelE,'description').text=yamlDt['description']
xml_tree.SubElement(channelE,'itunes:images',{'href':link_prefix+yamlDt['image']}).text=yamlDt['image']
xml_tree.SubElement(channelE,'language').text=yamlDt['language']
xml_tree.SubElement(channelE,'link').text=link_prefix
xml_tree.SubElement(channelE,'itunes:category',{'text':yamlDt['category']}).text=yamlDt['language']

for item in yamlDt['item']:
  item_element=xml_tree.SubElement(channelE,'item')
  xml_tree.SubElement(item_element,'title').text = yamlDt['title']
  xml_tree.SubElement(item_element,'itunes:author').text = yamlDt['author']
  xml_tree.SubElement(item_element,'description').text = item['description']
  xml_tree.SubElement(item_element,'itunes:duration').text = item['duration']
  xml_tree.SubElement(item_element,'pubDate').text = item['published']

  enclosure=xml_tree.SubElement(item_element,'enclosure',{
    'url':link_prefix + item['file'],
    'type':'audio/mpeg',
    'length': item['length']
  })

output=xml_tree.ElementTree(rsse)
output.write('podcast.xml',encoding='UTF-8',xml_declaration=True)
