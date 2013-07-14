client:
	cd chorescore-client && node_modules/grunt-cli/bin/grunt
	rm -rf chorescore-client/dist/tmp
	cp -pr chorescore-client/dist/* chorescore/static
