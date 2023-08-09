#!/bin/bash
cd ../dist/
nohup ./toaster -l &
rm nohup.out
cd -
