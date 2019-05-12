import xml.etree.ElementTree as ET
import os


voc_dir = 'dataset/voc-label/'
ctpn_dir = 'dataset/label/'


def voc2ctpn(voc_file, ctpn_file):
    lines = []
    with open(voc_file, 'r') as file:
        tree = ET.parse(file)
        root = tree.getroot()
        
        for obj in root.iter('object'):
            values = []
            bndbox = obj.find('bndbox')
            xmin = bndbox.find('xmin').text
            ymin = bndbox.find('ymin').text
            xmax = bndbox.find('xmax').text
            ymax = bndbox.find('ymax').text

            values.append(xmin)
            values.append(ymin)
            
            values.append(xmax)
            values.append(ymin)

            values.append(xmax)
            values.append(ymax)

            values.append(xmin)
            values.append(ymax)

            values.append('english')
            values.append('###')

            lines.append(','.join(values))

    with open(ctpn_file, 'w') as file:
        for line in lines:
            file.write(line + '\n')


if __name__ == "__main__":
    if not os.path.exists(ctpn_dir):
        os.makedirs(ctpn_dir)
    
    for filename in os.listdir(voc_dir):
        name, ext = os.path.splitext(filename)
        if ext.lower() != '.xml':
            continue
        
        voc_file = os.path.join(voc_dir, filename)
        ctpn_file = os.path.join(ctpn_dir, 'gt_{}.txt'.format(name))
        
        voc2ctpn(voc_file, ctpn_file)
