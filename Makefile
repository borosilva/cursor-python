remove-assets:
	pip3 uninstall -r requirements.txt -y

install-assets: remove-assets
	pip3 install -r requirements.txt
run:
	python3 -m cursor