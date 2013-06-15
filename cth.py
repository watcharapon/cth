from osv import osv, fields


class province(osv.osv):
    _name = 'cth.province'
    _columns = {
        'name': fields.char('Name', size=255, translate=True),
    }

province()

class district(osv.osv):
    _name = 'cth.district'
    _columns = {
        'name': fields.char('Name', size=255, translate=True),
        'province_ids': fields.many2one('cth.province', 'Province'),
    }

district()

class res_partners(osv.osv):
    _inherit = 'res.partner'
    _columns = {
        'province_id': fields.many2one('cth.province', 'Province'),
        'district_ids': fields.many2one('cth.district', 'District'),
    }

district()
