# edu3d.co
This was originally the development record of https://edu3d.co which aimed to be a PTE discussion forum. This project has completed the website is no longer maintained.

## Basic setting
The domain is parked on Bluehost <br>
The host is parked on AWS EC2 <br>
I used Bitnami image of Discourse <br>



Support channels <br>
* Bitnami documentation
* Bitnam forum 
* Discourse forum (which only supports the software itself, doesn't support docker environment and related problems)


### Configurations
* SMTP
* HTTPS
* Bind Bluehost domain on AWS EC2


### Extensions
Discourse support extensions in the forms of **theme components** and **plugins** <br>

For **Theme Components**, I used <br>


For **Plugins**, I used <br>

* discourse-adplugin

To install plugin, you need these commands.

```
cd /opt/bitnami/apps/discourse/htdocs <br>
sudo RAILS_ENV=production bundle exec rake plugin:install repo=PLUGIN_REPO_URL <br>
sudo RAILS_ENV=production bundle exec rake assets:precompile <br>
```

To unstall plugin, you need this
```
cd /opt/bitnami/apps/discourse/htdocs/plugins <br>
rm -rf PLUGIN-DIR <br>
sudo RAILS_ENV=production bundle exec rake assets:precompile <br>
```

### backup discourse
[Source](https://docs.bitnami.com/installer/apps/discourse/administration/backup-restore/)


### update discourse
[Source](https://docs.bitnami.com/google/apps/discourse/administration/upgrade/#keeping-in-sync-with-the-discourse-repository-at-github)

```
bundle _1.0.10_ -v # change bundle version is some errors happen, only valid once
gem uninstall bundler --version 1.16.6 # remove don't need version
gem list bundler # show all versions




sudo /opt/bitnami/ruby/bin/ruby bin/rake db:migrate RAILS_ENV=production
sudo chmod 666 log/production.log
sudo /opt/bitnami/ruby/bin/ruby bin/rake assets:precompile RAILS_ENV=production
sudo rm -rf tmp/cache
sudo /opt/bitnami/ctlscript.sh start

```

### change ownership
```
sudo chown bitnami {folder_name}
```


### start or stop services
[Source](https://docs.bitnami.com/aws/apps/discourse/administration/control-services/)
```
sudo /opt/bitnami/ctlscript.sh status
sudo /opt/bitnami/ctlscript.sh start
sudo /opt/bitnami/ctlscript.sh restart apache
sudo /opt/bitnami/ctlscript.sh stop
sudo /opt/bitnami/ctlscript.sh restart
```

### got passenger error 
check log file
```
tail /opt/bitnami/apache2/logs/error_log
```


### change built-in contents

https://github.com/discourse/discourse/blob/master/app/assets/javascripts/pretty-text/white-lister.js.es6

// add these these two html tags
export const DEFAULT_LIST = [
  "select",
  "option",
  "a.attachment",
  "a.hashtag",
