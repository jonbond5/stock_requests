# stock_requests
## This repo is being split into 2 since Alpha Vantage (https://alphavantage.co) has the tools I need already built
### Overview
Originally this was a repo for technical trading indicators.  Custom legacy indicators will be left in a 'legacy' branch, but moving forward I'll be using AlphaVantage.

## Installation
### Dependencies 
You can do these manually or via `install_dependencies.sh`

python 2

python 2:
 - requests
 - pandas
 - matplotlib
 - numpy

## Usage
### Grabbing AV key
Make sure you have an AV key (see link above to get one)

File `AV.txt` is NOT tracked by git - put just your key in there.

Get your key with `from get_av_key import get_av_key; get_av_key()`

## Reqs
- integrate AV tech analysis
- grab EDGAR filings to see major events
- query google every x mins for big news events

## Notes
EDGAR integration made possible by SEC

SEC CIKs (Central Index Key) downloaded from: https://

