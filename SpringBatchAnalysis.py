'''
Created on 2 feb 2017

@author: TGU
'''
import cast.analysers.jee
from cast.analysers import Bookmark
from xml.dom import minidom 
 
class SpringBatchAnalysis(cast.analysers.jee.Extension):
 
    def __init__(self):
        self.NbSpringBatchJobCreated = 0
        self.NbSpringBatchStepCreated = 0
 
    def start_analysis(self,options):
        
        #Save in the _local base the XML files 
        cast.analysers.log.info('Starting Spring Batch analysis')
        cast.analysers.log.info('=============== xpath batch ') 
        options.handle_xml_with_xpath('/beans')        # Spring Batch files
        
        
    def end_analysis(self):
        cast.analysers.log.info('Number of Spring job objects created : ' + str(self.NbSpringBatchJobCreated))
        cast.analysers.log.info('Number of Spring step objects created : ' + str(self.NbSpringBatchStepCreated))
                
    def start_xml_file(self,file):
        
        xmlfilepath = file.get_path() 
        
        if not file.get_path() or len(xmlfilepath.strip()) == 0: 
            return      
        
        if "web.xml" in xmlfilepath or "pom.xml" in xmlfilepath:
            return     
        
        cast.analysers.log.info('Scanning XML file : ' + xmlfilepath)
        self.analyseXMLSpringBatchFile(xmlfilepath, file)
            
    
    def analyseXMLSpringBatchFile(self, xmlfilepath, file):        
             
        cast.analysers.log.info('Scanning XML Spring Batch files ... : ' + xmlfilepath)

        with minidom.parse(xmlfilepath) as doc: 
            root = doc.documentElement
        
            for SpringBatch_job in root.getElementsByTagName('batch:job'):
                job_id =  SpringBatch_job.getAttribute('id')
                cast.analysers.log.info('job Id : ' + job_id)

                objectJob = cast.analysers.CustomObject()
                objectJob.set_name(job_id)
                objectJob.set_type('SpringBatchJob')
                objectJob.set_parent(file)
                objectJob.save()
                self.NbSpringBatchJobCreated += 1                
                bookmark = Bookmark(file, 1, 1, -1, -1) # TODO : find exact position 
                objectJob.save_position(bookmark)

                for SpringBatch_step in  SpringBatch_job.getElementsByTagName('batch:step'):
                    step_id = SpringBatch_step.getAttribute('id')
                    cast.analysers.log.info('==== step id : ' + step_id)
                    objectStep = cast.analysers.CustomObject()
                    objectStep.set_name(step_id)
                    objectStep.set_type('SpringBatchStep')
                    objectStep.set_parent(objectJob)
                    objectStep.save()
                    self.NbSpringBatchStepCreated += 1
                    bookmark = Bookmark(file, 1, 1, -1, -1) # TODO : find exact position 
                    objectStep.save_position(bookmark)
                    
                    tasklet_chunk = ''
                    
                    for SpringBatch_tasklet in SpringBatch_step.getElementsByTagName('batch:tasklet'):
                        step_tasklet = SpringBatch_tasklet.getAttribute('ref')
                        cast.analysers.log.info('======== tasklet ref : ' + step_tasklet)
                        step_tasklet_transaction_manager = SpringBatch_tasklet.getAttribute('transaction-manager')
                        cast.analysers.log.info('======== tasklet transaction-manager : ' + step_tasklet_transaction_manager)
                               
                        for SpringBatch_tasklet_chunk in SpringBatch_tasklet.getElementsByTagName('chunk'):
                            step_tasklet_chunk_reader = SpringBatch_tasklet_chunk.getAttribute('reader')
                            cast.analysers.log.info('======== tasklet chunk reader : ' + step_tasklet_chunk_reader) 
                            tasklet_chunk += step_tasklet_chunk_reader + "#"
                            step_tasklet_chunk_writer = SpringBatch_tasklet_chunk.getAttribute('writer')
                            cast.analysers.log.info('======== tasklet chunk writer : ' + step_tasklet_chunk_writer) 
                            tasklet_chunk += step_tasklet_chunk_writer + "#"
                            step_tasklet_chunk_processor = SpringBatch_tasklet_chunk.getAttribute('processor')
                            cast.analysers.log.info('======== tasklet chunk processor : ' + step_tasklet_chunk_processor) 
                            tasklet_chunk += step_tasklet_chunk_processor + "#"
                            cast.analysers.log.info('======== tasklet chunk : ' + tasklet_chunk)

                        for SpringBatch_tasklet_chunk in SpringBatch_tasklet.getElementsByTagName('batch:chunk'):
                            step_tasklet_chunk_reader = SpringBatch_tasklet_chunk.getAttribute('reader')
                            cast.analysers.log.info('======== tasklet chunk reader : ' + step_tasklet_chunk_reader) 
                            tasklet_chunk += step_tasklet_chunk_reader + "#"
                            step_tasklet_chunk_writer = SpringBatch_tasklet_chunk.getAttribute('writer')
                            cast.analysers.log.info('======== tasklet chunk writer : ' + step_tasklet_chunk_writer) 
                            tasklet_chunk += step_tasklet_chunk_writer + "#"
                            step_tasklet_chunk_processor = SpringBatch_tasklet_chunk.getAttribute('processor')
                            cast.analysers.log.info('======== tasklet chunk processor : ' + step_tasklet_chunk_processor) 
                            tasklet_chunk += step_tasklet_chunk_processor + "#"
                            cast.analysers.log.info('======== tasklet chunk : ' + tasklet_chunk)
                        
                    for SpringBatch_tasklet in SpringBatch_step.getElementsByTagName('tasklet'):
                        step_tasklet = SpringBatch_tasklet.getAttribute('ref')
                        cast.analysers.log.info('======== tasklet ref : ' + step_tasklet)   
                        step_tasklet_transaction_manager = SpringBatch_tasklet.getAttribute('transaction-manager')
                        cast.analysers.log.info('======== tasklet transaction-manager : ' + step_tasklet_transaction_manager) 
                    
                        for SpringBatch_tasklet_chunk in SpringBatch_tasklet.getElementsByTagName('chunk'):
                            step_tasklet_chunk_reader = SpringBatch_tasklet_chunk.getAttribute('reader')
                            cast.analysers.log.info('======== tasklet chunk reader : ' + step_tasklet_chunk_reader) 
                            tasklet_chunk += step_tasklet_chunk_reader + "#"
                            step_tasklet_chunk_writer = SpringBatch_tasklet_chunk.getAttribute('writer')
                            cast.analysers.log.info('======== tasklet chunk writer : ' + step_tasklet_chunk_writer) 
                            tasklet_chunk += step_tasklet_chunk_writer + "#"
                            step_tasklet_chunk_processor = SpringBatch_tasklet_chunk.getAttribute('processor')
                            cast.analysers.log.info('======== tasklet chunk processor : ' + step_tasklet_chunk_processor) 
                            tasklet_chunk += step_tasklet_chunk_processor + "#"
                            cast.analysers.log.info('======== tasklet chunk : ' + tasklet_chunk)

                        for SpringBatch_tasklet_chunk in SpringBatch_tasklet.getElementsByTagName('batch:chunk'):
                            step_tasklet_chunk_reader = SpringBatch_tasklet_chunk.getAttribute('reader')
                            cast.analysers.log.info('======== tasklet chunk reader : ' + step_tasklet_chunk_reader) 
                            tasklet_chunk += step_tasklet_chunk_reader + "#"
                            step_tasklet_chunk_writer = SpringBatch_tasklet_chunk.getAttribute('writer')
                            cast.analysers.log.info('======== tasklet chunk writer : ' + step_tasklet_chunk_writer) 
                            tasklet_chunk += step_tasklet_chunk_writer + "#"
                            step_tasklet_chunk_processor = SpringBatch_tasklet_chunk.getAttribute('processor')
                            cast.analysers.log.info('======== tasklet chunk processor : ' + step_tasklet_chunk_processor) 
                            tasklet_chunk += step_tasklet_chunk_processor + "#"
                            cast.analysers.log.info('======== tasklet chunk : ' + tasklet_chunk)                  
                    
                    objectStep.save_property('SpringBatchStep.step_tasklet', str(step_tasklet))
                    objectStep.save_property('SpringBatchStep.step_tasklet_transaction_manager', str(step_tasklet_transaction_manager))
                    objectStep.save_property('SpringBatchStep.step_tasklet_chunk', str(tasklet_chunk))

                    step_next = ''

                    for SpringBatch_next in SpringBatch_step.getElementsByTagName('batch:next'):
                        next_to = SpringBatch_next.getAttribute('to')
                        step_next += next_to + "#"
                        cast.analysers.log.info('======== next to : ' + next_to)
                                                
                    objectStep.save_property('SpringBatchStep.step_next', str(step_next))
    