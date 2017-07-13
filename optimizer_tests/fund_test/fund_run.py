####################
# fund test
####################


########################################
# !!!! You need to have github structure to run all the code without modificaiton.
########################################
# import all related functions

from optimizer_tests.fund_test.optimizer_fund_test import *



# generate fund_test_suite
fund_test_suite = get_fund_test_suite('2014-01-01')
fund_test_suite_large = get_fund_test_suite('2014-01-01', big = 1)
#len(fund_test_suite_large)

# run

bigboss = test_fund_opt(fund_test_suite)
bigboss_b_nc = test_fund_opt(fund_test_suite, 1)
bigboss_nb_c = test_fund_opt(fund_test_suite, 2)
bigboss_b_c = test_fund_opt(fund_test_suite, 3)



# to get efficient plots, run get_efficient_plot.py
get_efficient_plots(fund_test_suite, bigboss)
get_efficient_plots(fund_test_suite, bigboss_b_nc)
get_efficient_plots(fund_test_suite, bigboss_nb_c)
get_efficient_plots(fund_test_suite, bigboss_b_c)




########################################
# To save all the files for replicating next time


# one method is to save a small dic as txt

## 将返回的dictionary存成txt file
import json

with open('./figure/data/fund_test_suite_0705_148.txt', 'w') as file:
    file.write(json.dumps(fund_test_suite, ensure_ascii=False))

## 如需重新读入使用：
with open('./figure/data/fund_test_suite_0705_148.txt', 'r') as f:
    fund_test_suite = json.load(f)


# To save large dic (bigboss), use pickle file
import pickle
pickle.dump(bigboss, open( "././figure/data/bigboss_0705.p", "wb" ) )
pickle.dump(bigboss_b_nc, open( "././figure/data0705/bigboss_b_nc_0705.p", "wb" ) )
pickle.dump(bigboss_nb_c, open( "././figure/data0705/bigboss_nb_c_0705.p", "wb" ) )
pickle.dump(bigboss_b_c, open( "././figure/data0705/bigboss_b_c_0705.p", "wb" ) )


# To read it back to use again
bigboss = pickle.load(open( "./figure/data/bigboss_0705.p", "rb" ))



########################################

####################
# fund test after shrinkage
####################


# read in fund_test_suite
with open('./figure/data/fund_test_suite_0705_148.txt', 'r') as f:
    fund_test_suite = json.load(f)



import optimizer_tests.fund_test.optimizer_fund_test_cov_shrink as cm


cm0 = cm.test_fund_opt(fund_test_suite)
bigboss_b_nc = test_fund_opt(fund_test_suite, 1)
bigboss_nb_c = test_fund_opt(fund_test_suite, 2)
bigboss_b_c = test_fund_opt(fund_test_suite, 3)



# to get efficient plots, run get_efficient_plot.py
cm.get_efficient_plots(fund_test_suite, cm0)



q1 = cm.get_fund_test_suite('2014-01-01')
q2 = cm.get_fund_test_suite('2014-01-01')