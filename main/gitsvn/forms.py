from django import forms


class IssueCreateForm(forms.Form):
    LABELS_OPTIONS = [
        ("assigned", "Assigned"),
        ("inprogress", "In-progress"),
        ("completed", "Completed"),
        ("unassigned", "Un-assigned"),
    ]
    title = forms.CharField(
        max_length=50,
        required=True,
        help_text="Issue Title",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "id": "idIssueTitle",
                "name": "issueTitle",
            },
        ),
        # label="Issue Title",
    )
    description = forms.CharField(
        max_length=50,
        required=True,
        help_text="Issue Description",
        widget=forms.Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "id": "idIssueDesc",
                "name": "issueDesc",
            },
        ),
        # label="Issue Description",
    )
    labels = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "type": "checkbox",
                # "class": "form-check",
                "id": "idIssueLabels",
                "name": "issueLabels",
            },
        ),
        choices=LABELS_OPTIONS,
    )


class IssueGetIIDForm(forms.Form):
    iid = forms.CharField(
        required=True,
        help_text="Issue IID",
        widget=forms.TextInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "id": "idIssueID",
                "name": "issueIID",
            },
        ),
        label="Issue IID",
    )
