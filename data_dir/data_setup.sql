insert into source_category (category_name) values('Central');
insert into functional_category (functional_category_name) values('Financial');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('MCX','https://www.mcxindia.com/circulars/all-circulars','1','1','MCXScraper','content_heading');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('SEBI','https://www.sebi.gov.in/sebirss.xml','2','2','SEBIRSSCraper','content_heading');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('MSEI','https://www.msei.in/rss/rss?type=circular','2','2','MSEIRSSSCraper','content_heading');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('BSE','https://www.bseindia.com/data/xml/notices.xml','2','2','BSERSSScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('NSE','https://www.nseindia.com/api/circulars','2','2','NSEScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('RBI Press Releases','https://rbi.org.in/pressreleases_rss.xml','2','2','RBIScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('RBI Notifications','https://rbi.org.in/notifications_rss.xml','2','2','RBIScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('NCDEX Circulars','https://ncdex.com/circulars','2','2','NCDEXScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('NSDL Circulars','https://nsdl.co.in/business/circular.php','2','2','NSDLScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('CDSL','https://www.cdslindia.com/Publications/Communique.aspx','2','2','CDSLScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('SEBI Web Scraper','https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListingAll=yes','2','2','SEBIWebScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('MCLEAR','https://mclear.in','2','2','MCLEARScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('CCRL','https://www.ccrl.co.in/circulars.html','2','2','CCRLScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('NERL','https://www.nerlindia.com/circular','2','2','NERLScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('NISM','https://www.nism.ac.in/circulars','2','2','NISMScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('IFSCA','https://www.ifsca.gov.in/home/NewSection','2','2','IFSCAScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('UNSC','https://www.un.org/securitycouncil/sanctions/1267/press-releases','2','2','UNSCScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('UIDAI','https://uidai.gov.in/about-uidai/legal-framework/circulars.html','2','2','UIDAIScraper1','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('UIDAI','https://uidai.gov.in/media-resources/uidai-documents/circulars-memorandums-notification.html','2','2','UIDAIScraper2','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('APMI','https://www.apmiindia.org/apmi/welcome.htm','2','2','APMIScraper','content_url');

-- 25/11/2023
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('NSDL Issuers','https://nsdl.co.in/business/issuers_rts.php','2','2','NSDLIssuersScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('ICCL','https://www.icclindia.com/DynamicPages/NoticesCirculars.aspx','2','2','ICCLScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('MCXCCL','https://www.mcxccl.com/backpage.aspx/GetCircularAdvanceSearch','2','2','MCXCCLScraper','content_url');
insert into sources (source_name, source_url, source_category_id, functional_category_id, class_name, checkcolumn) values('NCCL','https://www.nccl.co.in/public/api/pagecontentbyid','2','2','NCCLScraper','content_url');
