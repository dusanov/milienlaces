General
=======
 * https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-editing/#ajax-example
 * missing pages:
    * index / filter / list all links for user
    * add / edit / delete link *ready for testing*
    * batch OOPS
 * delete link - set status to deleted
 * when adding link, set user to logged in user and hide it from add / update form *ready*
 * setting target on status change to ?
 * batch opps processing
 * validation on new link if the url is already in use *not ready* url.netloc/client/user/link_type - validation logic must be in overriden Model.clean() def clean(self): // try not to iterate over all objects but to filter on url.netloc (add netloc field to model and save it on insert) *ready*

App flow
========
 * on first hit, if not logged in, redirect to login page
 * on log out, redirect to login page

 Visual
 ======
 * top margin missing
 * proper bootstrap look and feel
 * top menu instead of left side menu
 * nice to have date range on filter form
 * more filter options: client status.
 * validation on form fields: dates...
 * sanitize data: self.cleaned_data['renewal_date'] * fix error msgs on link insert - tuples resolve name *ready* 
 * fix netloc read only shit
