from django.urls import path, include
from .router import DepartmentRouter, TicketRouter, TicketMessageRouter, TicketAttachmentRouter, CourseDepartmentRouter, CourseTicketRouter, CourseTicketMessageRouter, CourseTicketAttachmentRouter


app_name = 'Tickets'


department_router = DepartmentRouter()
ticket_router = TicketRouter()
ticket_message_router = TicketMessageRouter()
ticket_attachment_router = TicketAttachmentRouter()
course_department_router = CourseDepartmentRouter()
course_ticket_router = CourseTicketRouter()
course_ticket_message_router = CourseTicketMessageRouter()
course_ticket_attachment_router = CourseTicketAttachmentRouter()


urlpatterns = [
    path('departments/', include(department_router.get_urls())),
    path('tickets/', include(ticket_router.get_urls())),
    path('ticket-messages/', include(ticket_message_router.get_urls())),
    path('ticket-attachments/', include(ticket_attachment_router.get_urls())),
    path('course-departments/', include(course_department_router.get_urls())),
    path('course-tickets/', include(course_ticket_router.get_urls())),
    path('course-ticket-messages/', include(course_ticket_message_router.get_urls())),
    path('course-ticket-attachments/', include(course_ticket_attachment_router.get_urls())),
]
