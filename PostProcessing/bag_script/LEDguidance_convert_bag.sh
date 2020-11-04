#!/bin/bash
roscore &

sleep 3s

#f=`ls | grep *.bag`

#folder=`ls rec*`

files=`ls *bag`

<<COMMENT
for file in $files
do
    mkdir ${file%.*}
#files=`ls -F | grep /`
done
COMMENT

#<<COMMENT
for file in $files
do
    #nkf -u --overwrite $file
    #file=`ls `
    mkdir ${file%.*}
    file_name="${file%.*}"
    
    mv $file $file_name
    cd $file_name

    echo "$file converting..."
    sleep 1s

    rosbag info $file > ${file_name}_rosbag_info.txt
    echo "rosbag info recorded"

    #convert-bag-to-wav $file

    #rostopic echo -b $file -p /ecg/rri > ${file_name}_ecg_rri.csv
    #echo "/ecg/rri finished"
 
    #rostopic echo -b $file -p /dog_behavior_analyzer/predictions > ${file_name}_dog_behavior_analyzer_predictions.csv
    #echo "/dog_behavior_analyzer/predictions finished"

    rostopic echo -b $file -p /joy > ${file_name}_joy.csv
    echo "/joy finished"

  #  rostopic echo -b $file -p /imu/position > ${file_name}_imu_position.csv
   # echo "/imu/position finished"

    rostopic echo -b $file -p /spatial/posture > ${file_name}_spatial_posture.csv
    echo "/spatial/posture finished"

    #rostopic echo -b $file -p /imu/raw > ${file_name}_imu_mag.csv
    #echo "/imu/mag finished"

    rostopic echo -b $file -p /spatial/imu > ${file_name}_spatial_imu.csv
    echo "/spatial/imu finished"

    #rostopic echo -b $file -p /rosout > ${file_name}_rosout.csv
    #echo "/rosout finished"

    #rostopic echo -b $file -p /rosout_agg > ${file_name}_rosout_agg.csv
    #echo "/rosout_agg finished"

    #f=$1
    echo "$file finished"
    echo ""

    cd ..
done

#echo "$file_name"

#dir = ${$PWD}
#echo $PWD
#echo $(cd $(dirname $0) && pwd)

#dir=${file%\/*.c}
#rosbag info $file > rosbag_info.txt

#COMMENT

echo "Finished All"
