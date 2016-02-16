#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import sys;
import json;
import copy;


topic_word_dict = {};
current_word_list = [];
current_topic_no = 0;
TOP_WORDS=6
for line in open("./baike_lda_model_0.view_file"):
    if line.strip() == "" or line.startswith('http://'):
        continue;
    if line.startswith("TOPIC:"):
        if len(current_word_list) != 0:
            topic_word_dict[current_topic_no] = copy.deepcopy(current_word_list);
            del current_word_list[:]
        current_topic_no = int(line.strip().split(' ')[2]);
    else:
        if len(current_word_list) < TOP_WORDS:
            current_word_list.append(line.strip().split(' ')[0])

topic_word_dict[current_topic_no] = current_word_list;
#print json.dumps(topic_word_dict, ensure_ascii=False);

url_list = [];
for line in open("/home/disk0/wangbo01/study/tmp/baike-model/baike_split.seg.clean"):
    token_list = line.strip().split('\t');
    url_list.append(token_list[0])

line_no = 0;
for line in sys.stdin:
    token_list = line.strip().split(' ');
    max_iter = 0;
    i = 1;
    while i < len(token_list):
        if token_list[i] > token_list[max_iter]:
            max_iter = i;
        i = i + 1;
    print url_list[line_no] + "\tTOPIC:" + str(max_iter) + "\t" + ";".join(topic_word_dict[max_iter]);
    line_no = line_no + 1;
