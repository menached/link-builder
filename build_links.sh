#first empty all-property-links.txt
rm all-property-links.txt
python3 Discover/fetch_links.py
python3 Trinity/fetch_links.py
cat all-property-links.txt
