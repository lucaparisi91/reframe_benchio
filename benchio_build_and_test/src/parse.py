import re

testConditions = {
        "hdf5" :
            {
                "fullstriped" :
                {
                    "min_bandwidth" : 0.9,
                    "max_bandwidth" : 1.3
                }
            }
        }



def extract_timing( out ):
    pattern=r"Writing to (striped|unstriped|fullstriped)\/([a-z0-9]+)\.dat\W*\n time\W=\W+(\d.\d*)\W,\Wrate\W=\W+(\d.\d*)"
        
    prog = re.compile(pattern, re.IGNORECASE | re.MULTILINE )
    matches= prog.findall(out)

    result={}

    for match in matches:
        test=match[1]
        stripe=match[0]
        time=match[2]
        bandwidth=match[3]

        if not test in result:
            result[test]={}

        if not stripe in result[test]:
            result[test][stripe]={}
        
        result[test][stripe]["time"]=float(time)
        result[test][stripe]["bandwidth"]=float(bandwidth)

        #result[ test ]={ stripe :  { "time" : float(time), "bandwidh" : float(bandwidh) } }
    
    return(result)

def check_timing( outputResult, testConditions ):
    
    result=True 

    for test in testConditions:
        for stripe in testConditions[test]:
            min_bandwith=testConditions[test][stripe]["min_bandwidth"]
            max_bandwidth=testConditions[test][stripe]["max_bandwidth"]

            bandwidth = outputResult[test][stripe]["bandwidth"]


            result = result and (bandwidth>= min_bandwith) and (bandwidth <= max_bandwidth) 
    return result





if __name__ == "__main__":


    with open("rfm_job.out") as f:
        out=f.read()

        timePerfOut=extract_timing(out)


    testConditions = {
        "hdf5" :
            {
                "fullstriped" :
                {
                    "min_bandwidth" : 0.9,
                    "max_bandwidth" : 1.3
                }
            }
        }

    print(timePerfOut)


    print(check_timing(timePerfOut, testConditions) )