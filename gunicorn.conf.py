# docs at https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
import os

bind = f"0.0.0.0:{os.environ.get('PORT', 5050)}"

backlog = 64
workers = 3
worker_class = "gevent"
worker_connections = 1000
timeout = 50
keepalive = 5

spew = False

daemon = False
raw_env = []
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

proc_name = None

# Server hooks
#
#   post_fork - Called just after a worker has been forked.
#
#       A callable that takes a server and worker instance
#       as arguments.
#
#   pre_fork - Called just prior to forking the worker subprocess.
#
#       A callable that accepts the same arguments as after_fork
#
#   pre_exec - Called just prior to forking off a secondary
#       master process during things like config reloading.
#
#       A callable that takes a server instance as the sole argument.
def post_fork(server, worker):
    server.log.info(">>> 🦄 Worker spawned (pid: %s)", worker.pid)

def pre_fork(server, worker):
    pass

def pre_exec(server):
    server.log.info(">>> 🦄 Forked child, re-executing.")

def when_ready(server):
    server.log.info(">>> 🦄 Server is ready. Spawning workers")

def worker_int(worker):
    worker.log.info(">>> 🦄 Worker received INT or QUIT signal")

    ## get traceback info
    import threading, sys, traceback
    id2name = {th.ident: th.name for th in threading.enumerate()}
    code = []
    for threadId, stack in sys._current_frames().items():
        code.append("\n# Thread: %s(%d)" % (id2name.get(threadId,""),
            threadId))
        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append('File: "%s", line %d, in %s' % (filename,
                lineno, name))
            if line:
                code.append("  %s" % (line.strip()))
    worker.log.debug("\n".join(code))

def worker_abort(worker):
    worker.log.info(">>> 🦄 Worker received SIGABRT signal")

def ssl_context(conf, default_ssl_context_factory):
    import ssl

    # The default SSLContext returned by the factory function is initialized
    # with the TLS parameters from config, including TLS certificates and other
    # parameters.
    context = default_ssl_context_factory()

    # The SSLContext can be further customized, for example by enforcing
    # minimum TLS version.
    context.minimum_version = ssl.TLSVersion.TLSv1_3

    # Server can also return different server certificate depending which
    # hostname the client uses. Requires Python 3.7 or later.
    def sni_callback(socket, server_hostname, context):
        if server_hostname == "foo.127.0.0.1.nip.io":
            new_context = default_ssl_context_factory()
            new_context.load_cert_chain(certfile="foo.pem", keyfile="foo-key.pem")
            socket.context = new_context

    context.sni_callback = sni_callback

    return context