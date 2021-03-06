# trading-scripts
Various scripts for trading cryptocurrency

adjust_alerts_public.php 
is for when you have a bunch of alerts in coinigy but you want to go to sleep. The script goes through each of your alerts and adjusts them down some percentage you specify in the file. When you wake up the next day, you can run the script again with a higher percentage to raise the ones that didn't go off back up.

z_auto_sell_when_bought.py
is a very simple script for when you have a buy on bittrex set but you want to go to sleep and you'd like that buy to automatically go up for sale if it triggers before you wake up. For it to work, you have to download the bittrex python api wrapper here: https://github.com/ericsomdahl/python-bittrex The script is run from a terminal with the first argument being the symbol for the coin like ETH and the second argument being what you want to sell the coin for like 0.45354329 or something. It'll keep checking every couple of minutes for a quantity above zero for that coin and when it sees something, it puts it up for sale. The script only works for BTC pairs since that's all I trade but it's just a line or two to change for it to work for USDT and ETH.

z_alerts.py and z_get_alerts.php work together to alert you when Coinigy is lagging. z_get_alerts.php downloads all of your alerts from Coinigy and z_alerts.py runs in a loop checking bittrex for the latest prices. If the conditions are met for one of your Coinigy alerts, z_alerts.py lets you know. The files are hardcoded to work only with Bittrex and BTC pairs cuz that's all I trade but it isn't hard to modify them for all pairs and other exchanges. All you need to do is put your api key and secret for Coinigy into the z_get_alerts.php file and then run z_alerts.py.

z_base_scanner.py scans BTC pairs on Bittrex for bases and sets alerts in your Coinigy account. You put your key and secret into the file, run it and it will automatically find the bases and set the alerts in Coinigy for you. There are a few variables in the file you can fine tune like how many days to go back, whether bases should be based on low, close candles or in between, the quality of the base (higher quality gives you less bases), how far you want the alerts to be set from the base, etc.
