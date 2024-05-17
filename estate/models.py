from odoo import _, fields, api, models
import logging
import time

_logger = logging.getLogger('COUCOU')
class Coucou(models.Model):
    _name = "coucou.coucou"


    name = fields.Char()
    test = fields.Boolean(default=False)


    def _cron_stuff(self, batch_size=1):
        _logger.info('========do stuff here')
        stuff = self.search([('test', '=', False)], limit=batch_size)
        stuff.test = True
        time.sleep(1)
        test_count = self.search_count([('test', '=', False)])
        self.env['ir.cron']._notify_progress(done=batch_size, remaining=test_count)
        _logger.info('========finish stuff here %s', test_count)


    def populate_stuf(self):
        self.create([{'name': str(x)} for x in range(1000)])


    def trigger_test_cron(self):
        self.env.ref('estate.ir_cron_test')._trigger()


