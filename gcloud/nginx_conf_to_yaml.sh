kubectl create configmap nginx-via-proxy-conf --from-file nginx.conf -o yaml --dry-run > nginx.yaml
