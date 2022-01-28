#!/bin/bash
sh_file="${1}"
total_lines=$(wc -l "${sh_file}" | awk '{print $1}')
total_cycles=$((total_lines+3))
total_cycles=$((total_cycles/4))
total_cycles=$((total_cycles-1))

output_file="${sh_file}.txt"
touch "${output_file}"
for c in $(seq 0 ${total_cycles}) ; do
  echo "echo \"Launching 4xjobs : ${c}\""
  for sub in $(seq 0 3) ; do
    line_no=$((c*4+sub+1))
    line=$(sed -n ${line_no}p ${sh_file})
    if [ "${line}" == "" ] ; then
      line="echo \"no job\""
    fi
    echo "CUDA_VISIBLE_DEVICES=${sub} ${line} >> ${output_file} &"
    echo "p${sub}=\$!"
  done
  for sub in $(seq 0 3) ; do
    echo "wait \$p${sub}"
  done
done