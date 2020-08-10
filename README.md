## MY-web-edu3d.co

## Web Deployment
Bitnami image of Discourse


### Theme Components
discourse-

### Plugins
discourse-adplugin



### config SMTP

### config ssh

### install plugin
cd /opt/bitnami/apps/discourse/htdocs
sudo RAILS_ENV=production bundle exec rake plugin:install repo=PLUGIN_REPO_URL
sudo RAILS_ENV=production bundle exec rake assets:precompile


### uninstall plugin
cd /opt/bitnami/apps/discourse/htdocs/plugins
rm -rf PLUGIN-DIR
sudo RAILS_ENV=production bundle exec rake assets:precompile
