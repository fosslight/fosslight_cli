current_time=$(date +"%s")
./config.sh
fosslight-cli create project --prjName "test_$current_time" --osType Linux --distributionType 'General Model' --networkServerType N --priority P1
