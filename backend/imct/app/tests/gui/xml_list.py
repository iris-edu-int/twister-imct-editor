import unittest

from imct.app.tests.common.wgui import SeletiounTestMixin
from imct.app.tests.common import check_web_app_is_down


@unittest.skipIf(check_web_app_is_down(), "Application is down")
class XmlListTest(SeletiounTestMixin):

    EXT_QUERIES = {
        'xmlList':   "Ext.ComponentQuery.query('xml-list')",
        'xml_store': "Ext.ComponentQuery.query('xml-list')[0].store",
        'create_xml_btn': "Ext.ComponentQuery.query('xml-list #createXmlId')[0]",
        'delete_xml_btn': "Ext.ComponentQuery.query('xml-list #deleteXmlId')[0]",
        'create_xml_dlg': "Ext.ComponentQuery.query('xml-edit')",
        'create_xml_form': "Ext.ComponentQuery.query('xml-edit form')[0].form",
        'create_xml_form_btn': "Ext.ComponentQuery.query('xml-edit form button')[0]",
        'xml_bilder':  "Ext.ComponentQuery.query('xmlBuilder')",
    }

    TEST_XML = {
        'name': 'name',
        'source': 'source',
        'module': 'module',
        'url': 'http://www.imct.org',
        'sender': 'sender'
    }

    def test_create_and_delete_xml(self):
        # open page and check there is no record
        self.wait_js("{xmlList}.length>0".format(**self.EXT_QUERIES), 'There is no xml list panel!')
        self.assertTrue(self.driver.execute_script("return {xml_store}.getCount()==0".format(**self.EXT_QUERIES)), 'There is/are records in the store.')

        # open dialog and check there is default (url)
        self.click_component("{create_xml_btn}".format(**self.EXT_QUERIES))
        self.wait_js("{create_xml_dlg}.length>0".format(**self.EXT_QUERIES), 'There is no create xml dialog!')
        self.assertTrue("{create_xml_form}.getValues({test_xml}.url!='');".format(test_xml=self.TEST_XML, **self.EXT_QUERIES))

        # set values and save
        self.driver.execute_script("{create_xml_form}.setValues({test_xml});".format(test_xml=self.TEST_XML, **self.EXT_QUERIES))
        self.click_component("{create_xml_form_btn}".format(**self.EXT_QUERIES))
        self.wait_js("{xml_bilder}.length>0".format(**self.EXT_QUERIES), 'There is no xml builder panel!')

        # open page and check there is created record
        self.open_page("#xmls")
        self.wait_js("{xmlList}.length>0".format(**self.EXT_QUERIES), 'There is no xml list panel!')
        self.assertTrue(self.driver.execute_script("return {xml_store}.getCount()==1".format(**self.EXT_QUERIES)), 'There is no records in the store.')
        self.wait_while_load_mask(True)

        # delete record
        self.driver.execute_script("{xmlList}[0].getSelectionModel().select(0)".format(**self.EXT_QUERIES))
        self.wait_js("!{delete_xml_btn}.disabled".format(**self.EXT_QUERIES), 'Delete button is not enabled!')
        self.click_component("{delete_xml_btn}".format(**self.EXT_QUERIES))
        self.wait_js("{confirm_msg}.length>0".format(**self.BASE_EXT_QUERIES), 'There is no confirmation!')
        self.click_component("{cofirm_msg_btn}".format(**self.BASE_EXT_QUERIES))
        self.wait_while_load_mask(True)

        self.assertTrue(self.driver.execute_script("return {xml_store}.getCount()==0".format(**self.EXT_QUERIES)), 'There is/are records in the store.')


if __name__ == "__main__":
    unittest.main()
