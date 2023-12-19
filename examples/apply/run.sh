source ./increment_prj_version.sh
echo $PRJ_VERSION
fosslight-cli config set --server http://127.0.0.1:8180 --token eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiJhZG1pbiIsImVtYWlsIjoiYWRtaW5AZm9zc2xpZ2h0Lm9yZyJ9.3jWpmXwz73emxQ6tYjf1nkecLK3Br6Jth08trgF-gxQ
fosslight-cli apply -f create_project.yaml
