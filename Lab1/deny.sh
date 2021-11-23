#!/bin/bash
IFS=$'\n'
path=/root/templates.tbl
log=/root/log.txt
main_path=./
flag1=0
flag2=0
pflag=1
flag_forb=0
path_flag1=/root/flag1.tmp
path_flag2=/root/flag2.tmp
path_count=/root/count.tmp
path_pflag=/root/pflag.tmp
path_special=/root/special.tmp
path_forb=/root/forb.tmp
echo 0 >/root/flag1.tmp
echo 0 >/root/flag2.tmp
echo 0 >/root/count.tmp
echo 0 >/root/cpext.tmp
echo 0 >/root/cp.tmp
echo 1 >/root/pflag.tmp
echo -1 > /root/special.tmp
echo 0 > /root/forb.tmp
let count=0
file_past_ext=''
file_past=''
path_past=/root/past.tmp

>$log
for((;;)); do
        past=$cur
        cur=$(wc -l $log | cut -f 1 -d ' ')
        if [[ $past -ne $cur ]]
        then
                cat $log | while read p
                do
                        flag1=$(cat $path_flag1)
                        flag2=$(cat $path_flag2)
                        pflag=$(cat $path_pflag)
                        file_c_ext=$(echo $p | grep "Created" | grep -v "MovedTo" | cut -f 1 -d ' ' | sed 's@.*/@@')
                        file_c=$(echo $file_c_ext | cut -f 1 -d '.')
                        file_mt_ext=$(echo $p | grep "MovedTo" | cut -f 1 -d ' ' | sed 's@.*/@@')
                        file_mt=$(echo $file_mt_ext | cut -f 1 -d '.')
                        file_mf_ext=$(echo $p | grep "MovedFrom" | cut -f 1 -d ' ' | sed 's@.*/@@')
                        file_mf=$(echo $file_mf_ext | cut -f 1 -d '.')
                        file_cp_ext_tofile=$(echo $p | grep "PlatformSpecific" | cut -f 1 -d ' ' | sed 's@.*/@@')
                        file_cp_tofile=$(echo $file_cp_ext_tofile | cut -f 1 -d '.')
                        ## create forbidden
                        if [[ -n $file_c_ext ]] 
                        then
                                if grep -qw "$file_c" "$path" || grep -qw "$file_c_ext" "$path"  #with ext and without
                                then
                                        rm -rf $main_path$file_c_ext
                                fi
                        fi
                        ## rename from/to forbidden
                        if [[ -n $file_mt_ext ]] ## if we have "MovedTo" file
                        then
                                file_past_ext=$(cat $path_past)
                                if [[ -n $file_past_ext ]]
                                then
                                        file_past=$(echo $file_past_ext | cut -f 1 -d '.')
                                        if grep -qw "$file_past_ext" "$path" || grep -qw "$file_past" "$path" #from forb
                                        then
                                                if [[ $flag1 -eq 0 ]]
                                                then
                                                        mv $file_mt_ext $file_past_ext
                                                        echo 1 >$path_flag1
                                                fi
                                        fi
                                        if grep -qw "$file_mt_ext" "$path" || grep -qw "$file_mt" "$path" #to forb
                                        then
                                                if [[ $flag1 -eq 0 ]] 
                                                then
                                                        mv "$file_mt_ext" $file_past_ext
                                                        echo 1 >$path_flag1
                                                fi
                                        fi
                                fi
                                if [[ $flag2 -eq 1 ]]
                                then
                                        echo 0 >$path_flag1
                                        echo 0 >$path_flag2
                                fi
                        fi
                        ##for next iteration
                        if [[ -n $file_mf_ext ]] 
                        then
                                >$path_past
                                if [[ $flag1 -eq 0 ]] 
                                then
				echo $file_mf_ext > $path_past
                                fi
                                if [[ $flag1 -eq 1 ]]
                                then
                                        echo 1 >$path_flag2
                                fi
                        fi
                        #new copying
                        file_up_ext=$(echo $p | grep "Updated" | cut -f 1 -d ' ' | sed 's@.*/@@')
                        file_up=$(echo $file_up_ext | cut -f 1 -d '.')
                        special_counter=$(cat $path_special)
                        flag_forb=$(cat $path_forb)
                        if [[ -n $file_c_ext ]]
                        then
                                special_counter=0
                                echo $special_counter > $path_special
                        elif [[ $special_counter -eq 0 ]] && [[ -n $file_cp_ext_tofile ]]
                        then
                                special_counter=1
                                echo $special_counter > $path_special
                        elif [[ $special_counter -eq 1 ]] && [[ -n $file_cp_ext_tofile ]]
                        then
                                if grep -qw "$file_cp_tofile" "$path" || grep -qw "$file_cp_ext_tofile" "$path"
                                then
                                        flag_forb=1
                                        echo $flag_forb > $path_forb
                                fi
                                special_counter=2
                                echo $special_counter > $path_special

                        elif [[ $special_counter -eq 2 ]] && [[ -n $file_up_ext ]]
                        then
                                special_counter=3
                                echo $special_counter > $path_special
                        elif [[ $special_counter -eq 3 ]] && [[ -n $file_up_ext ]]
                        then
                                if [[ $flag_forb -eq 1 ]]
                                then
                                        rm -f "$file_up_ext"
                                        flag_forb=0
                                        echo $flag_forb > $path_forb
                                fi
                                special_counter=-1
                                echo $special_counter > $path_special
                        else
                                special_counter=-1
                                echo $special_counter > $path_special
                        fi

                done
                >$log
        fi
done
