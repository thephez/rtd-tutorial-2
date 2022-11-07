[block:callout] { “type”: “danger”, “body”: “**Warning:** A web browser
can access a HTTP REST interface running on localhost, possibly allowing
third parties to use cross-site scripting attacks to download your
transaction and block data, reducing your privacy. If you have privacy
concerns, you should not run a browser on the same computer as a
REST-enabled Dash Core node.”, “title”: “Privacy” } [/block] Dash Core
provides an **unauthenticated** HTTP REST interface. The interface runs
on the same port as the JSON-RPC interface, by default port 9998 for <>
and port 19998 for <>. It must be enabled by either starting Dash Core
with the ``-rest`` option or by specifying ``rest=1`` in the
configuration file. Make sure that the RPC interface is also activated.
Set ``server=1`` in ``dash.conf`` or supply the ``-server`` argument
when starting Dash Core. Starting Dash Core with ``dashd`` automatically
enables the RPC interface.

The interface is not intended for public access and is only accessible
from localhost by default. The interface uses standard `HTTP status
codes <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>`__ and
returns a plain-text description of errors for debugging.
