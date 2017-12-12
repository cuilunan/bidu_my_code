import os
from utils import str2bool, get_logger, get_entity

def conlleval(label_predict, label_path, metric_path):
    """

    :param label_predict:
    :param label_path:
    :param metric_path:
    :return:
    """
    eval_perl = "./conlleval_rev.pl"
    with open(label_path, "w", encoding='gb18030') as fw:
        line = []
        for sent_result in label_predict:
            tagList = []
            tag_list = []
            sentList = []
            for char, tag, tag_ in sent_result:
                #tag = '0' if tag == 'O' else tag
                #char = char
                sentList.append(char)
                tag_list.append(tag_)
                tagList.append(tag)
            sent_ = ''.join(sentList)
            Neg, Pos, Neu = get_entity(tag_list, sentList)
            #print(" ".join(Neg).encode('gb18030').decode('latin1'))
            line.append("{}\t{}\t{}\t{}\n".format(sent_, 'Neg: '+' '.join(Neg), 'Pos: '+' '.join(Pos), 'Neu: '+' '.join(Neu)))
            #print (line)
            line.append("\n")
        fw.writelines(line)
    os.system("perl {} < {} > {}".format(eval_perl, label_path, metric_path))
    """
    recall_0 = 0.001
    recall_1 = 0.001
    recall_2 = 0.001
    pre_0 = 0.001
    pre_1 = 0.001
    pre_2 = 0.001
    true_0 = 0.001
    true_1 = 0.001
    true_2 = 0.001
    for sent_result in label_predict:
        for char, tag, tag_ in sent_result:
            if int(tag) == 0 and int(tag_) == 0:
                recall_0 += 1
                pre_0 += 1
                true_0 += 1
            if int(tag) == 0 and int(tag_) == 1:
                recall_0 += 1
                pre_1 += 1
            if int(tag) == 0 and int(tag_) == 2:
                recall_0 += 1
                pre_2 += 1
            if int(tag) == 1 and int(tag_) == 1:
                recall_1 += 1
                pre_1 += 1
                true_1 += 1
            if int(tag) == 1 and int(tag_) == 0:
                recall_1 += 1 
                pre_0 +=1
            if int(tag) == 1 and int(tag_) == 2:
                recall_1 += 1
                pre_2 += 1
            if int(tag) == 2 and int(tag_) == 2:
                recall_2 += 1
                pre_2 += 1
                true_2 += 1
            if int(tag) == 2 and int(tag_) == 0:
                recall_2 += 1
                pre_0 += 1
            if int(tag) == 2 and int(tag_) == 1:
                recall_2 += 1
                pre_1 += 1
    recallOf_0 = true_0/float(recall_0)
    preOf_0 = true_0/float(pre_0)
    recallOf_1 = true_1/float(recall_1)
    preOf_1 = true_1/float(pre_1)
    recallOf_2 = true_2/float(recall_2)
    preOf_2 = true_2/float(pre_2)
    recallOf_ave = (recallOf_0 + recallOf_1 + recallOf_2)/3.0
    preOf_ave = (preOf_0 + preOf_1 + preOf_2)/3.0
    with open(metric_path,'w') as f:
        f.write("recall of 0:"+str(recallOf_0)+"  precision of 0:"+str(preOf_0)+'\n' \
                "recall of 1:"+str(recallOf_1)+"  precision of 1:"+str(preOf_1)+'\n' \
                "recall of 2:"+str(recallOf_2)+"  precision of 2:"+str(preOf_2)+'\n' \
                "recall of ave:"+str(recallOf_ave)+"  precision of ave:"+str(preOf_ave)+'\n' )
    """
    with open(metric_path) as fr:
        metrics = [line for line in fr]
    return metrics
    
