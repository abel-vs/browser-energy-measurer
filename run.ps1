sleep 10
#warm-up runs
.'C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe' -file ".\eval\edge_run_0.csv" -cmd python .\src\edge.py
.'C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe' -file ".\eval\chrome_run_0.csv" -cmd python .\src\chrome.py
.'C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe' -file ".\eval\firefox_run_0.csv" -cmd python .\src\firefox.py
sleep 30
$i=0
While ($i -le 10)
    {
    #batch 3 edge runs
    $j=1
    While ($j -le 3)
        {
        $filename = [string]::Format(“.\eval\edge_run_{0}.csv",$i*3+$j)
        .'C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe' -file $filename -cmd python .\src\edge.py
        $j++
        }
    sleep 30
    #batch 3 chrome runs
    $j=1
    While ($j -le 3)
        {
        $filename = [string]::Format(“.\eval\chrome_run_{0}.csv",$i*3+$j)
        .'C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe' -file $filename -cmd python .\src\chrome.py
        $j++
        }
    sleep 30
    #batch 3 firefox runs
    $j=1
    While ($j -le 3)
        {
        $filename = [string]::Format(“.\eval\firefox_run_{0}.csv",$i*3+$j)
        .'C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe' -file $filename -cmd python .\src\firefox.py
        $j++
        }
    sleep 30
    $i++
    }
 