
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random


im = Image.new("RGB", (2500,2000), (255,255,255))

draw = ImageDraw.Draw(im, 'RGBA')

data = [
	{'year' : '1820', 'figure' : 8385},
	{'year' : '1821', 'figure' : 9127},
	{'year' : '1822', 'figure' : 6911},
	{'year' : '1823', 'figure' : 6354},
	{'year' : '1824', 'figure' : 7912},
	{'year' : '1825', 'figure' : 10199},
	{'year' : '1826', 'figure' : 10837},
	{'year' : '1827', 'figure' : 18875},
	{'year' : '1828', 'figure' : 27382},
	{'year' : '1829', 'figure' : 22520},
	{'year' : '1830', 'figure' : 23322},
	{'year' : '1831', 'figure' : 22633},
	{'year' : '1832', 'figure' : 48386},
	{'year' : '1833', 'figure' : 58640},
	{'year' : '1834', 'figure' : 65365},
	{'year' : '1835', 'figure' : 45374},
	{'year' : '1836', 'figure' : 76242},
	{'year' : '1837', 'figure' : 79340},
	{'year' : '1838', 'figure' : 38914},
	{'year' : '1839', 'figure' : 68069},
	{'year' : '1840', 'figure' : 84066},
	{'year' : '1841', 'figure' : 80289},
	{'year' : '1842', 'figure' : 104565},
	{'year' : '1843', 'figure' : 69994},
	{'year' : '1844', 'figure' : 78615},
	{'year' : '1845', 'figure' : 114371},
	{'year' : '1846', 'figure' : 154416},
	{'year' : '1847', 'figure' : 234968},
	{'year' : '1848', 'figure' : 226527},
	{'year' : '1849', 'figure' : 297024},
	{'year' : '1850', 'figure' : 295984},
	{'year' : '1851', 'figure' : 379466},
	{'year' : '1852', 'figure' : 371603},
	{'year' : '1853', 'figure' : 368645},
	{'year' : '1854', 'figure' : 427833},
	{'year' : '1855', 'figure' : 200877},
	{'year' : '1856', 'figure' : 200436},
	{'year' : '1857', 'figure' : 251306},
	{'year' : '1858', 'figure' : 123126},
	{'year' : '1859', 'figure' : 121282},
	{'year' : '1860', 'figure' : 153640},
	{'year' : '1861', 'figure' : 91918},
	{'year' : '1862', 'figure' : 91985},
	{'year' : '1863', 'figure' : 176282},
	{'year' : '1864', 'figure' : 193418},
	{'year' : '1865', 'figure' : 248120},
	{'year' : '1866', 'figure' : 318568},
	{'year' : '1867', 'figure' : 315722},
	{'year' : '1868', 'figure' : 277680},
	{'year' : '1869', 'figure' : 352768},
	{'year' : '1870', 'figure' : 387203},
	{'year' : '1871', 'figure' : 321350},
	{'year' : '1872', 'figure' : 404806},
	{'year' : '1873', 'figure' : 459803},
	{'year' : '1874', 'figure' : 313339},
	{'year' : '1875', 'figure' : 227498},
	{'year' : '1876', 'figure' : 169986},
	{'year' : '1877', 'figure' : 141857},
	{'year' : '1878', 'figure' : 138469},
	{'year' : '1879', 'figure' : 177826},
	{'year' : '1880', 'figure' : 457257},
	{'year' : '1881', 'figure' : 669431},
	{'year' : '1882', 'figure' : 788992},
	{'year' : '1883', 'figure' : 603322},
	{'year' : '1884', 'figure' : 518595},
	{'year' : '1885', 'figure' : 395346},
	{'year' : '1886', 'figure' : 334203},
	{'year' : '1887', 'figure' : 490109},
	{'year' : '1888', 'figure' : 546889},
	{'year' : '1889', 'figure' : 444427},
	{'year' : '1890', 'figure' : 455302},
	{'year' : '1891', 'figure' : 560319},
	{'year' : '1892', 'figure' : 579663},
	{'year' : '1893', 'figure' : 439730},
	{'year' : '1894', 'figure' : 285631},
	{'year' : '1895', 'figure' : 258536},
	{'year' : '1896', 'figure' : 343267},
	{'year' : '1897', 'figure' : 230832},
	{'year' : '1898', 'figure' : 229299},
	{'year' : '1899', 'figure' : 311715},
	{'year' : '1900', 'figure' : 448572},
	{'year' : '1901', 'figure' : 487918},
	{'year' : '1902', 'figure' : 648743},
	{'year' : '1903', 'figure' : 857046},
	{'year' : '1904', 'figure' : 812870},
	{'year' : '1905', 'figure' : 26499},
	{'year' : '1906', 'figure' : 100499},
	{'year' : '1907', 'figure' : 285349},
	{'year' : '1908', 'figure' : 782870},
	{'year' : '1909', 'figure' : 751786},
	{'year' : '1910', 'figure' : 41570},
	{'year' : '1911', 'figure' : 878587},
	{'year' : '1912', 'figure' : 838172},
	{'year' : '1913', 'figure' : 197892},
	{'year' : '1914', 'figure' : 218480},
	{'year' : '1915', 'figure' : 326700},
	{'year' : '1916', 'figure' : 298826},
	{'year' : '1917', 'figure' : 295403},
	{'year' : '1918', 'figure' : 110618},
	{'year' : '1919', 'figure' : 141132},
	{'year' : '1920', 'figure' : 430001},
	{'year' : '1921', 'figure' : 805228},
	{'year' : '1922', 'figure' : 309556},
	{'year' : '1923', 'figure' : 522919},
	{'year' : '1924', 'figure' : 706896},
	{'year' : '1925', 'figure' : 294314},
	{'year' : '1926', 'figure' : 304488},
	{'year' : '1927', 'figure' : 335175},
	{'year' : '1928', 'figure' : 307255},
	{'year' : '1929', 'figure' : 279678},
	{'year' : '1930', 'figure' : 241700},
	{'year' : '1931', 'figure' : 97139},
	{'year' : '1932', 'figure' : 35576},
	{'year' : '1933', 'figure' : 23068},
	{'year' : '1934', 'figure' : 29470},
	{'year' : '1935', 'figure' : 34956},
	{'year' : '1936', 'figure' : 36329},
	{'year' : '1937', 'figure' : 50244},
	{'year' : '1938', 'figure' : 67895},
	{'year' : '1939', 'figure' : 82998},
	{'year' : '1940', 'figure' : 70756},
	{'year' : '1941', 'figure' : 51776},
	{'year' : '1942', 'figure' : 28781},
	{'year' : '1943', 'figure' : 23725},
	{'year' : '1944', 'figure' : 28551},
	{'year' : '1945', 'figure' : 38119},
	{'year' : '1946', 'figure' : 108721},
	{'year' : '1947', 'figure' : 147292},
	{'year' : '1948', 'figure' : 170570},
	{'year' : '1949', 'figure' : 188317},
	{'year' : '1950', 'figure' : 249187},
	{'year' : '1951', 'figure' : 205717},
	{'year' : '1952', 'figure' : 265520},
	{'year' : '1953', 'figure' : 170434},
	{'year' : '1954', 'figure' : 208177},
	{'year' : '1955', 'figure' : 237790},
	{'year' : '1956', 'figure' : 321625},
	{'year' : '1957', 'figure' : 326867},
	{'year' : '1958', 'figure' : 253265},
	{'year' : '1959', 'figure' : 260686},
	{'year' : '1960', 'figure' : 265398},
	{'year' : '1961', 'figure' : 271344},
	{'year' : '1962', 'figure' : 283763},
]

# VARIABLES------------------

#coordinates	
x = 1
y = 490

#color
h = random.randrange(0,255)
i = random.randrange(0,255)
j = random.randrange(0,255)

# ARCS-------------------------

for line in data:
	degree = (line['figure'])/2441

	draw.arc((x,x,y,y),0,degree,fill=(h,i,j))

	x = x+10
	y = y+10

	h = random.randrange(0,255)
	i = random.randrange(0,255)
	j = random.randrange(0,255)


# DATES----------------------

fontPath = 'open-sans/OpenSans-Regular.ttf'
font = ImageFont.truetype(fontPath, 50)

lat = 576
lon = 278

draw.text( (475,180),"1820", fill=(0), font=font)

draw.text( (lat, lon), '1830', fill=(0), font=font)
draw.text( ((lat+100), (lon+100)), '1840', fill=(0), font=font)
draw.text( ((lat+250), (lon+200)), '1850', fill=(0), font=font)
draw.text( ((lat+375), (lon+300)), '1860', fill=(0), font=font)
draw.text( ((lat+500), (lon+400)), '1870', fill=(0), font=font)
draw.text( ((lat+600), (lon+500)), '1880', fill=(0), font=font)
draw.text( ((lat+700), (lon+600)), '1890', fill=(0), font=font)
draw.text( ((lat+800), (lon+700)), '1900', fill=(0), font=font)
draw.text( ((lat+900), (lon+800)), '1910', fill=(0), font=font)
draw.text( ((lat+975), (lon+900)), '1920', fill=(0), font=font)
draw.text( ((lat+1050), (lon+1000)), '1930', fill=(0), font=font)
draw.text( ((lat+1100), (lon+1100)), '1940', fill=(0), font=font)
draw.text( ((lat+1200), (lon+1200)), '1950', fill=(0), font=font)

draw.text( (1900,1600),'1962', fill=(0), font=font)

im.show()

im.save("mydatavis.png")

