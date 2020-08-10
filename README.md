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
cd /opt/bitnami/apps/discourse/htdocs <br>
sudo RAILS_ENV=production bundle exec rake plugin:install repo=PLUGIN_REPO_URL <br>
sudo RAILS_ENV=production bundle exec rake assets:precompile <br>


### uninstall plugin
cd /opt/bitnami/apps/discourse/htdocs/plugins <br>
rm -rf PLUGIN-DIR <br>
sudo RAILS_ENV=production bundle exec rake assets:precompile <br>


<select>
  <option>Ok</option>
  <option>NotOk</option>
</select>
