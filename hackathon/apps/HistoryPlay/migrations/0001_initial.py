# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Answer'
        db.create_table(u'HistoryPlay_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answer_set', to=orm['HistoryPlay.Question'])),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('is_correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('HistoryPlay', ['Answer'])

        # Adding model 'Category'
        db.create_table(u'HistoryPlay_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('HistoryPlay', ['Category'])

        # Adding model 'HistoryPlay'
        db.create_table(u'HistoryPlay_historyplay', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(related_name='history_play_set', to=orm['HistoryPlay.Place'])),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(related_name='history_play_set', to=orm['HistoryPlay.Profile'])),
            ('progress', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('HistoryPlay', ['HistoryPlay'])

        # Adding model 'Place'
        db.create_table(u'HistoryPlay_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='place_set', to=orm['HistoryPlay.Category'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('web_page', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('schedule', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('cost', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('latitud', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('longitud', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('step', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('HistoryPlay', ['Place'])

        # Adding model 'Profile'
        db.create_table(u'HistoryPlay_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('HistoryPlay', ['Profile'])

        # Adding model 'Question'
        db.create_table(u'HistoryPlay_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(related_name='question_set', to=orm['HistoryPlay.Place'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('HistoryPlay', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Answer'
        db.delete_table(u'HistoryPlay_answer')

        # Deleting model 'Category'
        db.delete_table(u'HistoryPlay_category')

        # Deleting model 'HistoryPlay'
        db.delete_table(u'HistoryPlay_historyplay')

        # Deleting model 'Place'
        db.delete_table(u'HistoryPlay_place')

        # Deleting model 'Profile'
        db.delete_table(u'HistoryPlay_profile')

        # Deleting model 'Question'
        db.delete_table(u'HistoryPlay_question')


    models = {
        'HistoryPlay.answer': {
            'Meta': {'object_name': 'Answer'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'is_correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answer_set'", 'to': "orm['HistoryPlay.Question']"})
        },
        'HistoryPlay.category': {
            'Meta': {'object_name': 'Category'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'HistoryPlay.historyplay': {
            'Meta': {'object_name': 'HistoryPlay'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'history_play_set'", 'to': "orm['HistoryPlay.Place']"}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'history_play_set'", 'to': "orm['HistoryPlay.Profile']"}),
            'progress': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'HistoryPlay.place': {
            'Meta': {'object_name': 'Place'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'place_set'", 'to': "orm['HistoryPlay.Category']"}),
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'longitud': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'schedule': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'step': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'web_page': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'HistoryPlay.profile': {
            'Meta': {'object_name': 'Profile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'HistoryPlay.question': {
            'Meta': {'object_name': 'Question'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'question_set'", 'to': "orm['HistoryPlay.Place']"}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['HistoryPlay']