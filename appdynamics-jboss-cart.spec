%global cartridgedir %{_libexecdir}/openshift/cartridges/appdynamics-jboss-cart

Summary:       An appdynamics cartridge to publishes metrics for your Jboss (AS,EAP,EWS) application to the AppDynamics controller.
Name:          appdynamics-jboss-cart
Version: 1.0.6
Release:       1%{?dist}
Group:         Applications/Internet
License:       ASL 2.0
URL:           http://www.openshift.com
Source0:    http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz 
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
BuildArch:     noarch

%description
Provides AppDynamics agent cartridge support. 

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%files
%dir %{cartridgedir}
%{cartridgedir}/metadata
%{cartridgedir}/versions
#%{cartridgedir}/env
%{cartridgedir}/template
%{cartridgedir}/usr
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/conf/
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Tue Mar 03 2015 Unknown name 1.0.6-1
- more changed spec file (kunal@myubuntu.(none))

* Tue Mar 03 2015 Unknown name 1.0.5-1
- more changed spec file (kunal@myubuntu.(none))

* Tue Mar 03 2015 Unknown name 1.0.4-1
- changed spec file (kunal@myubuntu.(none))

* Tue Mar 03 2015 Unknown name 1.0.3-1
- 

* Tue Mar 03 2015 Unknown name 1.0.1-1
- new package built with tito


