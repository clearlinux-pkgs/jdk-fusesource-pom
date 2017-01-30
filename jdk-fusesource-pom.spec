Name     : jdk-fusesource-pom
Version  : 1.9
Release  : 1
URL      : http://repo1.maven.org/maven2/org/fusesource/fusesource-pom/1.9/fusesource-pom-1.9.pom
Source0  : http://repo1.maven.org/maven2/org/fusesource/fusesource-pom/1.9/fusesource-pom-1.9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-apache-parent-data
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-resource-bundles
BuildRequires : jdk-apache-parent
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-parent
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-artifact-resolver
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-remote-resources-plugin
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-resources
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy-java
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
BuildRequires : jdk-snappy
BuildRequires : jdk-xz
#BuildRequires : jdk-
#BuildRequires : jdk-
#BuildRequires : jdk-
#BuildRequires : jdk-
#BuildRequires : jdk-
#BuildRequires : jdk-
#BuildRequires : jdk-
#BuildRequires : jdk-

%description
No detailed description available

%prep
cp %{SOURCE0} pom.xml

python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin :clirr-maven-plugin
python3 /usr/share/java-utils/pom_editor.py pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-webdav-jackrabbit']]"


%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n fusesource-pom -d %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/fusesource-pom.xml
/usr/share/maven-poms/fusesource-pom/fusesource-pom.pom
