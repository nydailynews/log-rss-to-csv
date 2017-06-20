#!/bin/bash
workon ORATV
alias deployqa='cd ~/work/oratv-video/www/; scp -r ./ qa:/apps/video'
alias deployprod='cd ~/work/oratv-video/www/; scp -r ./ prod:/apps/video'
