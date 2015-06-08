%title: cmail
%shouts: Shouts to #kitinfo

# Project
cmail-mta, Mail processing suite with SQLite backend
>cmail.rocks | github.com/cmail-mta
>devel@cmail.rocks

# Speakers
mpease on freenode
>me@mpease.de

cbdev on freenode, hackint, quakenet
>dev.cbcdn.com | cb@cbcdn.com



-------------------------------------------------
# Underserved use-case

\* Simple maildomain (maybe more than one)
\* Flexible address -> Mailbox mapping
\* Non-system users need access (POP, IMAP)
\* Simple forwarding mail server

-------------------------------------------------
# Recognize this?

    root@s2:~# wc -l /etc/exim4/exim4.conf
    1993 /etc/exim4/exim4.conf


-------------------------------------------------
# Most MTAs

\* Huge configuration
\* 99+ Tutorials, all different
\* Difficult to get "right"
\* SMTP, POP, IMAP in separate modules
\* Interfaces not clearly specified
\* Densely feature-packed
\* \> 50 kLoC

-------------------------------------------------
# Project Goals

\* Split configuration
 \* Module-specific (Ports, TLS, Limits)
 \* Run-time: Users, Addresses, etc
\* Quick & easy setup
\* Intuitive administration & configuration
\* Lightweight
\* Clear interfaces

-------------------------------------------------
# Example config file

	verbosity 3
	logfile /var/log/cmail/msa.log
	user cmail
	group cmail
	database /home/cmail/master.db3
	
	bind * 25 announce=lolmail.lol
	bind :: 25 announce=lolmail.lol size=5242880
	bind * 587 auth=tlsonly,strict announce=lolmail.lol \
	 cert=/etc/cmail/keys/tls-mail.cert \
	 key=/etc/cmail/keys/tls-mail.key \
	 ciphers=NORMAL:%LATEST_RECORD_VERSION:-VERS-SSL3.0
	bind :: 587 auth=tlsonly,strict announce=lolmail.lol \
	 cert=/etc/cmail/keys/tls-mail.cert \
	 key=/etc/cmail/keys/tls-mail.key \
	 ciphers=NORMAL:%LATEST_RECORD_VERSION:-VERS-SSL3.0

-------------------------------------------------
# Runtime config stored in SQLite

\* Great API
\* Easy access
\* Lots of tools
\* File-based -> Easy backup & handling
\* Can be replaced live

-------------------------------------------------
# Code Stats

\* SMTP server: 2 kLoC
\* POP server: 1.5 kLoC
\* SMTP client: 1.5 kLoC
\* HTTP API: 2.5 kLoC
\* Overall: 11 kLoC (~7k C, ~3.5k Web)

-------------------------------------------------
# Architecture


-------------------------------------------------
# Runtime Administration

\* cmail-admin: Command-line tool
\* SQLite database editors: Choose your own
\* Web Panel: Use your browser!
 \* Accesses cmail-api
 \* Includes interfaces for all modules
 \* Intuitive interface for live configuration
 \* Allows delegation of privileges to users
  \* Users can administer their own domains!
 \* Includes simulated routing test

-------------------------------------------------
# Cool stuff

\* Address regexes
\* Flexible routing system
\* (Planned) Plugin API
\* Web Panel
\* User databases


-------------------------------------------------
# Runtime stats

\* ~10 active instances
\* Maildrops up to 4000 mails
\* LKML for testing ;)
\* Pretty reliable so far

-------------------------------------------------
# How can you help

\* Website
\* Test infrastructure & Tests
\* Packaging
\* Feedback

