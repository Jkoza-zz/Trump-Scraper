logDir=/home/ec2-user/logs
scriptDir=/home/ec2-user/trump-scraper

python ${scriptDir}/scraper.py > ${logDir}/scraper.log 2>&1
python ${scriptDir}/upload.py > ${logDir}/scraper.log 2>&1