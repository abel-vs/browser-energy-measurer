$i=1
While ($i -le 10)
    {
    $filename = [string]::Format(“edge_run_{0}.csv",$i)
    .'C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe' -file $filename -cmd python .\src\main.py
    $i++
    }
   