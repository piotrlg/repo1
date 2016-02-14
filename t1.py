__author__ = 'piotrlg'


class kl(object):
    stat_atr = 0

    def __init__(self, meth_atr):
        kl.stat_atr = kl.stat_atr + 1
        self.meth_atr = meth_atr
        self.meth_atr = self.meth_atr + 1


inst1 = kl(1)
inst2 = kl(2)

print 'klass atr', kl.stat_atr
print 'meth atr1', inst1.meth_atr
print 'meth atr2', inst2.meth_atr