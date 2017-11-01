"""this is the main part of the assignment"""

# Copyright 2017 Mengxi Wang wmx@bu.edu

import unittest
import subprocess
import math
import sys
import timeout_decorator

#please change this to valid author emails
AUTHORS = ['wmx@bu.edu']
PROGRAM_TO_TEST = "collisionc"

@timeout_decorator.timeout(1)
def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,timeout=1)

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)




class CollisionTestCase(unittest.TestCase):
    "empty class - write this"
    def setUp(self):
        pass
#        self.assertFalse(PROGRAM_TO_TEST.endswith('hard'),"")
#        self.assertTrue(PROGRAM_TO_TEST.endswith('27'),"")
    def teardown(self):
        pass
    
    def float_check(self,out,arg_num,ball_num):
        out_corrected=""
        temp = out.split('\n')
        for target in range(0,(1+ball_num)*arg_num,ball_num+1):
            if float(temp[target])-math.floor(float(temp[target]))==0:
                temp[target] = str(math.floor(float(temp[target])))

        for i in range(len(temp)):
            out_corrected = out_corrected + temp[i]
            if i < len(temp)-1:
                out_corrected = out_corrected+"\n"
        return out_corrected

    def test_one(self):
        strin = "one 20 10 -2 1"
        correct_out = "3\none 14 13 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        out = self.float_check(out,1,1)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_notnumber(self):
        strin = "one one two -2 1"
        correct_out = ""
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,1)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    
    def test_invalid(self):
        strin = "one 0 0 1 0 15 0 -1 0"
        correct_out = ""
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2.5"],strin)
        self.assertEqual(rc,1)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    
    def test_commend(self):
        strin = "one 20 10 -2 1"
        correct_out = ""
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["three"],strin)
        self.assertEqual(rc,2)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    
    def test_empty(self):
        strin = "one 20 10 -2 1"
        correct_out = ""
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,[""],strin)
        self.assertEqual(rc,2)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

#    def test_twoballs(self):
#        strin = "one 0 0 1 0\ntwo 15 0 -1 0"
#        correct_out = "2.5\none 2.5 0 1 0\ntwo 12.5 0 -1 0\n"
#        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2.5"],strin)
#        out = self.float_check(out,1,2)
#        self.assertEqual(rc,0)
#        self.assertEqual(out,correct_out)
#        self.assertEqual(errs,"")

    def test_after(self):
        strin = "one 0 0 1 0\ntwo 15 0 -1 0"
        correct_out = "5\none 0 0 -1 0\ntwo 15 0 1 0\n" 
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["5"],strin) 
        out = self.float_check(out,1,2)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    
#    def test_two(self):
#        strin = "one 5 0 -5 0\ntwo 0 15 0 -5"
#        correct_out = "1\none 0 0 -5 -5\ntwo 0 10 0 0\n"
#        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
#        self.assertEqual(rc,0)
#        self.assertEqual(out,correct_out)
#        self.assertEqual(errs,"")

    def test_before(self):
        strin = "one 0 0 1 0\ntwo 15 0 -1 0"
        correct_out = "2\none 2 0 1 0\ntwo 13 0 -1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2"],strin)
        out = self.float_check(out,1,2)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_threeballs(self):
        strin = "one 0 0 1 0\ntwo 15 0 -1 0\nthree 0 35 0 -5"
        correct_out = "5\none 0 0 -1 0\ntwo 15 0 1 0\nthree 0 10 0 -5\n" 
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["5"],strin)
        out = self.float_check(out,1,3)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    
    def test_threeballs_after(self):
        strin = "one 0 0 1 0\ntwo 15 0 -1 0\nthree -35 0 5 0"
        correct_out = "6\none 5 0 5 0\ntwo 16 0 1 0\nthree -11 0 -1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["6"],strin)
        out = self.float_check(out,1,3)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    
    def test_three(self):
        strin = "one 0 0 3 4\ntwo 40 0 -3 4\nthree 80 0 -3 4"       
        correct_out = "6\none 12 24 -3 4\ntwo 28 24 3 4\nthree 62 24 -3 4\n11\none -3 44 -3 4\ntwo 37 44 -3 4\nthree 53 44 3 4\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,['6','11'],strin)
        out = self.float_check(out,2,3)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
        
    def test_four(self):
        strin = "one -20 0 3 4\ntwo 0 0 3 4\nthree 40 0 -3 4\nfour 80 0 -3 4"       
        correct_out = "11\none -13 44 -3 4\ntwo 23 44 3 4\nthree 37 44 -3 4\nfour 53 44 3 4\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["11"],strin)
        out = self.float_check(out,1,4)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
        
    def test_digit(self):
        strin="one 1.1111 2.4111 2.5 3.6"
        correct_out="2\none 6.1111 9.6111 2.5 3.6\n"
        (rc,out,errs)=runprogram(PROGRAM_TO_TEST,['2'],strin)
        out=self.float_check(out,1,1)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    
    def test_bignumber(self):
        strin="one 11111111 11111111 10000000 0"
        correct_out="1\none 21111111 11111111 10000000 0\n"
        (rc,out,errs)=runprogram(PROGRAM_TO_TEST,['1'],strin)
        out=self.float_check(out,1,1)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    
    def test_bigout(self):
        strin = "one 20 10 1 0"
        correct_out = "10000000\none 10000020 10 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["10000000"],strin)
        out = self.float_check(out,1,1)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
        
    def test_manyballs(self):
        strin = "one 0 0 1 0\ntwo 0 1 -1 0\nthree 0 2 1 0\nfour 0 3 -1 0\nfive 0 4 1 0\nsix 0 5 1 0\nseven 0 6 1 0\neight 0 7 1 0\nnine 0 8 1 0\nten 0 9 1 0\neleven 0 10 1 0\ntweleve 0 11 1 0"
        correct_out = "1\none 1 0 1 0\ntwo -1 1 -1 0\nthree 1 2 1 0\nfour -1 3 -1 0\nfive 1 4 1 0\nsix 1 5 1 0\nseven 1 6 1 0\neight 1 7 1 0\nnine 1 8 1 0\nten 1 9 1 0\neleven 1 10 1 0\ntweleve 1 11 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        out = self.float_check(out,1,11)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    
    def test_bigsmallout(self):
        strin = "one 0 0 1 0"       
        correct_out = "1\none 1 0 1 0\n10000000\none 10000000 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,['10000000','1'],strin)
        out = self.float_check(out,2,1)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
        
    def test_zero(self):
        strin = "one 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0"       
        correct_out = "1\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,['1'],strin)
        out = self.float_check(out,1,12)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
        
    def test_programname(self):
        self.assertTrue(PROGRAM_TO_TEST.startswith('col'),"wrong program name")

def main():
    "show how to use runprogram"

    print(runprogram('./test_program.py', ["4", "56", "test"], "my input"))
    unittest.main()

if __name__ == '__main__':
    main()
