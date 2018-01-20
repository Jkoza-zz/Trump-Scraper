logDir=/home/ec2-user/logs
scriptDir=/home/ec2-user/Trump-Scraper

python ${scriptDir}/scraper.py > ${logDir}/scraper.log 2>&1
echo "scraped"
python ${scriptDir}/upload.py > ${logDir}/scraper.log 2>&1
echo "uploaded"
