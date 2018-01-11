logDir=/home/ec2-user/logs
scriptDir=/home/ec2-user/sophi-social-scraper

time=$(date +"%Y-%m-%d_%T")
year="$(date +%Y)"
month="$(date +%m)"
day="$(date +%d)"
hour="$(date +%H)"

while getopts ":i:u:p:d:c:s:" o; do
    case "${o}" in
        s)
            src=${OPTARG}
            ;;
        i)
            ip=${OPTARG}
            ;;
        u)
            username=${OPTARG}
            ;;
        p)
            password=${OPTARG}
            ;;
        d)
            database=${OPTARG}
            ;;
        c)
            collection=${OPTARG}
            ;;
    esac
done

if [ -z "${ip}" ]
	then
		echo "ip not provided"
		exit
fi

if [ -z "${username}" ]
	then
		echo "username not provided"
		exit
fi

if [ -z "${password}" ]
	then
		echo "password not provided"
		exit
fi

if [ -z "${database}" ]
	then
		echo "database not provided"
		exit
fi

if [ -z "${collection}" ]
	then
		echo "collection not provided"
		exit
fi

if [ -z "${src}" ]
	then
		echo "source not provided"
		exit
fi

#upload to mongo
touch ${scriptDir}/${src}_data/${src}_${time}.csv
python ${scriptDir}/scripts/${src}.py ${scriptDir}/${src}_data/${src}_${time}.csv > ${scriptDir}/${src}-scraper.log 2>&1
python ${scriptDir}/upload.py -f=${scriptDir}/${src}_data/${src}_${time}.csv -i=${ip} -u=${username} -p=${password} -db=${database} -c=${collection} 
echo "scraped ${src} and uploaded to MongoDB at host ${ip} in the ${database} database (${collection} collection)"

#upload to s3 (backup)
gzip ${scriptDir}/${src}_data/${src}_${time}.csv
aws s3 cp ${scriptDir}/${src}_data/${src}_${time}.csv.gz s3://tgam.omniture/rliu/social_scraper/year=${year}/month=${month}/day=${day}/hour=${hour}/${src}/${src}_${time}.csv.gz
rm -f ${scriptDir}/${src}_data/*